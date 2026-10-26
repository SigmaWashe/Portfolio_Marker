import datetime, io, zipfile

from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import get_valid_filename

from core.base import ReportGenerator, REPORT_TEMPLATES
from core.subjects import SUBJECT_CALC
from core.utils import get_center_number
from student.forms import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')

            user.student.name = name.strip().capitalize()
            user.student.surname = surname.strip().capitalize()

            center_number = get_center_number(user.student.exam_num)
            school = Schools.objects.filter(center_number=center_number).first()

            if school:
                user.student.school = school.name_of_school
                user.student.save()

            user.student.subjects.set([9, 10, 15])

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('select_subjects')
        else:
            print(" FORM ERRORS:", form.errors.as_data())
    else:
        form = SignupForm()

    return render(request, 'student/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('student:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'student/signin.html', {'form': form})


def logouts(request):
    logout(request)
    return redirect('student:login')


@login_required(login_url='student:login')
def complete_profile(request):
    if hasattr(request.user, 'student'):
        return redirect('student:dashboard')

    if request.method == 'POST':
        exam_number = request.POST.get('exam_number')
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        if not exam_number or not name or not surname:
            return render(request, 'student/complete_profile.html', {'error': 'All fields are required.'})

        if Student.objects.filter(exam_num=exam_number).exists():
            return render(request, 'student/complete_profile.html', {'error': 'Exam number already registered.'})

        Student.objects.create(user=request.user, exam_num=exam_number, name=name, surname=surname)
        return redirect('student:dashboard')

    return render(request, 'student/complete_profile.html')


@login_required(login_url='student:login')
def select_subjects(request):
    student = request.user.student
    current_subjects = [
        {
            'id': subject.id,
            'name': subject.subject,
            'icon': SUBJECT_CHOICES.get(subject.id, {}).get('icon', 'book'),
            'slug': subject.subject.lower().replace(' ', '-'),
            'average': float(
                Test.objects.filter(subject=subject.id).aggregate(average=Avg("percentage", default=0))["average"]),
        }
        for subject in student.subjects.all()
    ]

    if request.method == 'POST':
        form = SubjectForm(request.POST, student=student)
        if form.is_valid():
            selected_subjects = form.cleaned_data['subjects']
            Test.objects.filter(student=student).exclude(subject__in=selected_subjects).delete()

            student.subjects.set(selected_subjects)
            return redirect('student:dashboard')
    else: form = SubjectForm(student=student)

    context = { 'form': form, 'student': student, 'current_subjects': current_subjects, }

    return render(request, 'student/select_subjects.html', context)


@login_required(login_url='student:login')
def dashboard(request):
    student = request.user.student

    current_subjects = [
        {
            'id'  : subject.id,
            'name': subject.subject,
            'icon': SUBJECT_CHOICES.get(subject.id, {}).get('icon', 'book'),
            'slug': subject.subject.lower().replace(' ', '-'),
            'report' : subject.id in REPORT_TEMPLATES,
            'average': float(Test.objects.filter(subject=subject.id).aggregate(average=Avg("percentage", default=0))["average"]),
        }
        for subject in student.subjects.all()
    ]

    total_tests = Test.objects.filter(student=student).count()
    avg = Test.objects.filter(student=student).aggregate(Avg('weighted'))

    avg_percentage = round(avg['weighted__avg'], 1) if avg['weighted__avg'] else None

    context =  {
        'student': student,
        'total_tests': total_tests,
        'avg_percentage': avg_percentage,
        'current_subjects': current_subjects,
    }

    return render(request, 'student/dashboard.html', context)


@login_required(login_url='student:login')
def subject(request, subject_name):
    student = request.user.student
    subject = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))

    tests = Test.objects.filter(student=student, subject_id=subject.id).order_by('date')

    total_weighted = sum(test.weighted for test in tests)

    current_subjects = [
        {
            'id': subject.id,
            'name': subject.subject,
            'icon': SUBJECT_CHOICES.get(subject.id, {}).get('icon', 'book'),
            'slug': subject.subject.lower().replace(' ', '-'),
        }
        for subject in student.subjects.all()
    ]
    test_choices = SUBJECT_CHOICES.get(subject.id, {}).get('choices', [])

    TestsFormset = modelformset_factory(Test, form=UpdateTests, extra=0)
    formset = TestsFormset(queryset=tests, form_kwargs={'subject': subject.id})

    context = {
        'student': student,
        'subject': subject,
        'formset': formset,
        'tests': tests,
        'total_weighted': round_decimal(total_weighted, 2),
        'current_subjects': current_subjects,
        'test_choices': test_choices,
        'report_available': subject.id in REPORT_TEMPLATES,
    }

    return render(request, 'student/subject.html', context)


@login_required(login_url='student:login')
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
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else timezone.now().date()

    percentage, weighted = calc(test_id, mark, total)

    Test.objects.create(student=student, subject_id=subject_id, type=test_id, description=desc, mark=mark, total=total,
                        weighted=round_decimal(weighted, 2),  percentage=round_decimal(percentage, 2),
                        symbol=assign_symbol(percentage), date=date,)

    return redirect('student:subject', subject_name=subject_name)


@login_required(login_url='student:login')
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
        Test.objects.create(student=student, subject_id=subject_id, type=int(test_id), description=desc, mark=float(mark),
                            total=int(total), weighted=round_decimal(weighted, 2), percentage=round_decimal(percentage, 2),
                            symbol=assign_symbol(percentage), date=submission_date,)
    return redirect('student:subject', subject_name=subject_name)


@login_required(login_url='student:login')
def manage_tests(request, subject_name):
    student = request.user.student
    subject = get_object_or_404(Subject, subject__iexact=subject_name.replace('-', ' '))
    tests = Test.objects.filter(student=student, subject=subject).order_by('date')
    calculator = SUBJECT_CALC.get(subject.id)

    TestsFormset = modelformset_factory(Test, form=UpdateTests, extra=0)

    if request.method == 'POST':
        formset = TestsFormset(request.POST, queryset=tests, form_kwargs={'subject':subject.id})

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    type = int(form.cleaned_data.get('type'))
                    date = form.cleaned_data.get('date')
                    mark = float(form.cleaned_data.get('mark') or 0)
                    total = int(form.cleaned_data.get('total') or 50)
                    description = form.cleaned_data.get('description')
                    percentage, weighted = calculator(type or 1, mark, total)

                    Test.objects.update_or_create(id=form.instance.pk, student=student, subject=subject, defaults=
                    {'type': type, 'mark': mark, 'total': total, 'weighted': round_decimal(weighted, 2),
                     'date': date, 'percentage': round_decimal(percentage, 2), 'symbol': assign_symbol(percentage), 'description': description})

            return redirect('student:subject', subject_name=subject_name)
    else:
        formset = TestsFormset(queryset=tests, form_kwargs={'subject':subject.id})

    total_weighted = sum(t.weighted for t in tests)

    context = {
        'student': student,
        'formset': formset,
        'subject': subject,
        'tests'  : tests,
        'total_weighted': round_decimal(total_weighted, 2),
        'report_available': subject.id in REPORT_TEMPLATES,
    }

    return render(request, 'student/subject.html', context)


@login_required(login_url='student:login')
def subject_delete(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))

    record_id = int(request.POST['id'])
    Test.objects.filter(student=student, subject_id=sub.id, test_id=record_id).delete()
    return redirect('student:subject', subject_name=subject_name)


@login_required(login_url='student:login')
def preview_report(request, subject_name):
    student = request.user.student
    sub = Subject.objects.get(subject__iexact=subject_name.replace('-', ' '))
    subject_id = sub.id

    tests = Test.objects.filter(student=student, subject_id=subject_id)
    gen = ReportGenerator(student, tests)

    if not gen.has_template(subject_id):
        return HttpResponse("No report template available for this subject yet.", status=400)

    buffer = gen.generate(subject_id)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'inline; filename="preview.docx"'
    return response


@login_required(login_url='student:login')
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


@login_required(login_url='student:login')
def generate_all(request):
    student = request.user.student
    subjects = student.subjects.all()

    if not subjects.exists():
        return HttpResponse("No subjects to generate SBA cover sheets for.", status=400)

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for subject in subjects:
            tests = Test.objects.filter(student=student, subject_id=subject.id)
            gen = ReportGenerator(student, tests)

            if not gen.has_template(subject.id):
                return HttpResponse("No report template available for this subject yet.", status=400)

            pdf = gen.generate_pdf(subject.id)
            if hasattr(pdf, 'getvalue'): pdf = pdf.getvalue()

            name = get_valid_filename(f"{student.surname}_{student.name}_{subject.subject}.pdf")
            zf.writestr(name, pdf)
            pass

    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{get_valid_filename(
                                      f"{student.surname}_{student.name}")}_reports.zip"'
    return response