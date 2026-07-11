import datetime
import json

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST

from student.models import Test, Student, Subject, Schools, ChosenSubjects
from core.subjects import *
from core.base import ReportGenerator, REPORT_TEMPLATES
from core.utils import get_center_number
from student.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            center_number = get_center_number(user.student.exam_num)
            school = Schools.objects.filter(center_number=center_number).first()

            if school:
                user.student.school = school.name_of_school
                user.student.save()

            ChosenSubjects.objects.get_or_create(student=user.student)

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('select_subjects')
        else:
            print(" FORM ERRORS:", form.errors.as_data())
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def logins(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logouts(request):
    logout(request)
    return redirect('login')


@login_required
def select_subjects(request):
    student = request.user.student

    if request.method == 'POST':
        subject_ids = [int(i) for i in request.POST.getlist('subjects')]

        if len(subject_ids) < 3:
            active_map = {sub.id: sub.subject for sub in Subject.objects.filter(id__in=subject_ids)}
            return render(request, 'select_subjects.html', {
                'subjects': Subject.objects.all(),
                'error': 'Please select at least 3 subjects.',
                'active_map_json': json.dumps(active_map),
            })

        chosen = student.chosen_subjects
        for subject_id, field in SUBJECT_FIELDS.items():
            setattr(chosen, field, subject_id in subject_ids)
        chosen.save()
        student.save()
        return redirect('dashboard')

    active_map = {
        sub.id: sub.subject
        for sub in Subject.objects.all()
        if getattr(student.chosen_subjects, SUBJECT_FIELDS[sub.id], False)
    }

    return render(request, 'select_subjects.html', {
        'subjects': Subject.objects.all(),
        'active_map_json': json.dumps(active_map),
    })


@login_required
def complete_profile(request):
    if hasattr(request.user, 'student'):
        return redirect('dashboard')

    if request.method == 'POST':
        exam_number = request.POST.get('exam_number')
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        if not exam_number or not name or not surname:
            return render(request, 'account/complete_profile.html', {'error': 'All fields are required.'})

        if Student.objects.filter(exam_num=exam_number).exists():
            return render(request, 'account/complete_profile.html', {'error': 'Exam number already registered.'})

        Student.objects.create(user=request.user, exam_num=exam_number, name=name, surname=surname)
        return redirect('dashboard')

    return render(request, 'account/complete_profile.html')


@login_required
def dashboard(request):
    student = request.user.student

    active_subjects = [
        {
            'id': sub.id,
            'name': sub.subject,
            'icon': SUBJECT_CHOICES.get(sub.id, {}).get('icon', 'book'),
            'slug': sub.subject.lower().replace(' ', '-'),
        }
        for sub in Subject.objects.all()
        if getattr(student.chosen_subjects, SUBJECT_FIELDS.get(sub.id, ''), False)
    ]

    total_tests = Test.objects.filter(student=student).count()
    avg = Test.objects.filter(student=student).aggregate(Avg('percentage'))
    avg_percentage = round(avg['percentage__avg'], 1) if avg['percentage__avg'] else None

    return render(request, 'dashboard.html', {
        'student': student,
        'total_tests': total_tests,
        'avg_percentage': avg_percentage,
        'active_subjects': active_subjects,
    })


@login_required
def subject(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    tests = Test.objects.filter(student=student, subject_id=subject_id).order_by('submission_date')

    for test in tests: test.symbol_info = assign_symbol(test.percentage, as_dict=True)

    total_weighted = sum(t.weighted_mark for t in tests)

    active_subjects = [
        {
            'id': s.id,
            'name': s.subject,
            'icon': SUBJECT_CHOICES.get(s.id, {}).get('icon', 'book'),
            'slug': s.subject.lower().replace(' ', '-'),
        }
        for s in Subject.objects.all()
        if getattr(student.chosen_subjects, SUBJECT_FIELDS.get(s.id, ''), False)
    ]
    test_choices = SUBJECT_CHOICES.get(subject_id, {}).get('choices', [])

    return render(request, 'subject.html', {
        'student': student,
        'subject': sub,
        'tests': tests,
        'total_weighted': round_decimal(total_weighted, 2),
        'active_subjects': active_subjects,
        'test_choices': test_choices,
        'report_available': subject_id in REPORT_TEMPLATES,
    })


@login_required
@require_POST
def subject_insert(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    calc = SUBJECT_CALC.get(subject_id)
    test_id = int(request.POST['test_id'])
    desc = request.POST.get('desc', '')
    mark = float(request.POST['mark'])
    total = int(request.POST['total'])
    date_str = request.POST.get('submission_date')
    submission_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else timezone.now().date()

    percentage, weighted = calc(test_id, mark, total)

    Test.objects.create(
        student=student,
        subject_id=subject_id,
        test_type=test_id,
        test_description=desc,
        actual_mark=mark,
        possible_mark=total,
        weighted_mark=round_decimal(weighted, 2),
        percentage=round_decimal(percentage, 2),
        symbol=assign_symbol(percentage),
        submission_date=submission_date,
    )
    return redirect('subject', subject_name=subject_name)


@login_required
@require_POST
def subject_insert_all(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    calc = SUBJECT_CALC.get(subject_id)
    test_ids = request.POST.getlist('test_id[]')
    descs = request.POST.getlist('desc[]')
    marks = request.POST.getlist('mark[]')
    totals = request.POST.getlist('total[]')

    dates = request.POST.getlist('submission_date[]')
    for test_id, desc, mark, total, date_str in zip(test_ids, descs, marks, totals, dates):
        if not mark or not total:
            continue
        submission_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else timezone.now().date()
        percentage, weighted = calc(int(test_id), float(mark), int(total))
        Test.objects.create(
            student=student,
            subject_id=subject_id,
            test_type=int(test_id),
            test_description=desc,
            actual_mark=float(mark),
            possible_mark=int(total),
            weighted_mark=round_decimal(weighted, 2),
            percentage=round_decimal(percentage, 2),
            symbol=assign_symbol(percentage),
            submission_date=submission_date,
        )
    return redirect('subject', subject_name=subject_name)


@login_required
@require_POST
def subject_delete(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))

    record_id = int(request.POST['id'])
    Test.objects.filter(student=student, subject_id=sub.id, test_id=record_id).delete()
    return redirect('subject', subject_name=subject_name)


@login_required
def preview_report(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    tests = Test.objects.filter(student=student, subject_id=subject_id)
    gen = ReportGenerator(student, tests)

    if not gen.has_template(subject_id):
        return HttpResponse("No report template available for this subject yet.", status=400)

    buffer = gen.generate(subject_id)
    response = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'inline; filename="preview.docx"'
    return response


@login_required
def generate_report(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    tests = Test.objects.filter(student=student, subject_id=subject_id)
    gen = ReportGenerator(student, tests)

    if not gen.has_template(subject_id):
        return HttpResponse("No report template available for this subject yet.", status=400)

    buffer = gen.generate_pdf(subject_id)
    template_name = REPORT_TEMPLATES[subject_id].replace('.docx', '')
    filename = f"{student.surname}_{student.exam_num}_{template_name}.pdf"

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response