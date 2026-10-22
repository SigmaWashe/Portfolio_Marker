import io
import zipfile

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import get_valid_filename

from core.base import ReportGenerator, REPORT_TEMPLATES
from core.subjects import REPORT_TEMPLATES
from teacher.forms import *
from teacher.models import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = form.cleaned_data.get('subject')
            school  = form.cleaned_data.get('school')
            request.session['subject_id'] = subject.id
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('teacher:dashboard')
        else:
            print(" FORM ERRORS:", form.errors.as_data())
    else:
        form = SignupForm()
    return render(request, 'teacher/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('teacher:dashboard')
        else:
            return render(request, 'teacher/signin.html', {'error': 'Invalid email or password.'})
    return render(request, 'teacher/signin.html')


def signout(request):
    logout(request)
    return redirect('teacher:login')


@login_required(login_url='teacher:login')
def dashboard(request):
    teacher  = request.user.teacher
    tests    = teachers_tests(teacher)
    students = teachers_students(teacher)

    current_students = [
        {
            'id'       : student.id,
            'exam_num' : student.exam_num,
            'full_name': f"{student.name} {student.surname}",
            'average'  : student_average(student),
        }
        for student in students
    ]

    current_tests = [
        {
            'id': test.id,
            'date': test.date,
            'type': test_type(teacher.subject.id, test.type),
            'total'  : test.total,
            'average': test_average(teacher, test.id),
            'description': test.description,
        }
        for test in tests
    ]

    context = {
        'tests'  : current_tests,
        'teacher': teacher,
        'students': current_students,
        'number_students': students.count(),
    }

    return render(request, 'teacher/dashboard.html', context)


@login_required(login_url='teacher:login')
def students(request):
    teacher = request.user.teacher
    tests = teachers_tests(teacher)
    students = teachers_students(teacher)
    StudentsFormset = modelformset_factory(Student, form=UpdateStudents, extra=0)

    if request.method == 'POST':
        formset = StudentsFormset(request.POST, queryset=students)

        if formset.is_valid():
            all_valid = True
            for form in formset:
                if form.cleaned_data:
                    name = form.cleaned_data.get('name')
                    surname = form.cleaned_data.get('surname')
                    exam_num = form.cleaned_data.get('exam_num')

                    center_num = get_center_number(int(exam_num))
                    school = Schools.objects.filter(center_number=center_num).first()

                    if school != teacher.school:
                        form.add_error('exam_num', 'This exam number belongs to a different school.')
                        all_valid = False
                        continue

                    student, _ = Student.objects.update_or_create(exam_num=exam_num, defaults={'name': name, 'surname': surname, 'school': school}, )
                    for test in tests: Marks.objects.get_or_create(test=test, student=student)

            if all_valid:
                return redirect('teacher:dashboard')
    else:
        formset = StudentsFormset(queryset=students)

    return render(request, 'teacher/student.html', {'formset': formset})


@login_required(login_url='teacher:login')
def create_test(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)

    type = request.POST.get('type')
    description = request.POST.get('description')
    date = request.POST.get('date')
    total = request.POST.get('total')

    test = Tests.objects.create(teacher=teacher, subject=teacher.subject, type=type, description=description, total=total, date=date,)
    for student in students: Marks.objects.create(test=test, student=student,)

    return redirect('teacher:students')


@login_required(login_url='teacher:login')
def manage_tests(request):
    teacher = request.user.teacher
    tests = teachers_tests(teacher)
    students = teachers_students(teacher)

    TestsFormset = modelformset_factory(Tests, form=UpdateTests, extra=0)

    if request.method == 'POST':
        formset = TestsFormset(request.POST, queryset=tests, form_kwargs={'teacher': teacher})
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    type        = form.cleaned_data.get('type')
                    description = form.cleaned_data.get('description')
                    total       = form.cleaned_data.get('total')
                    date        = form.cleaned_data.get('date')
                    Tests.objects.update_or_create(id=form.instance.pk, teacher=teacher, subject=teacher.subject, defaults={
                       'subject': teacher.subject, 'teacher': teacher, 'type': type, 'description': description, 'total': total, 'date': date,
                    })
            return redirect('teacher:dashboard')
    else:
        formset = TestsFormset(queryset=tests, form_kwargs={'teacher': teacher})

    context = {
        'teacher' : teacher,
        'tests'   : tests,
        'students': students,
        'formset' : formset,
        'average' : subject_average(teacher),
    }
    return render(request, 'teacher/manage_tests.html', context)


@login_required(login_url='teacher:login')
def manage_marks(request):
    teacher    = request.user.teacher
    form       = ManageMarks(request.POST or None, teacher=teacher)
    tests      = teachers_tests(teacher)
    marks      = student_marks(teacher)
    students   = teachers_students(teacher)
    calculator = SUBJECT_CALC.get(teacher.subject)

    current_students = [
        {
            'id': student.id,
            'name'    : student.name,
            'surname' : student.surname,
            'exam_num': student.exam_num,
            'average' : student_average(student),
        }
        for student in students
    ]

    if request.method == 'POST' and form.is_valid():
        test = form.cleaned_data.get('tests')
        total = test.total

        for student in students:
            mark_key = f'mark_{student.id}'
            mark = request.POST.get(mark_key)

            if mark in (None, ''): continue

            percentage, weighted = calculator(test.type, mark, total)

            Marks.objects.update_or_create(test=test, student=student, defaults={
                'mark': mark, 'weighted': round_decimal(weighted, 2), 'percentage': round_decimal(percentage, 2),
                'symbol': assign_symbol(percentage), })
            pass

    context = {
        'teacher' : teacher,
        'tests'   : list(tests.values('id', 'total')),
        'form'    : form,
        'marks'   : list(marks.values('test_id', 'student_id', 'mark')),
        'students': current_students,
        'average' : subject_average(teacher),
    }
    return render(request, 'teacher/manage_marks.html', context)


@login_required(login_url='teacher:login')
def preview_report(request, student_id):
    teacher = request.user.teacher
    student = get_object_or_404(Student, pk=student_id)

    marks = Marks.objects.filter(test__teacher=teacher, student=student)
    tests = Tests.objects.filter(teacher=teacher, subject_id=teacher.subject.id)
    gen = ReportGenerator(student, tests, teacher, marks)

    if not gen.has_template(teacher.subject.id):
        return HttpResponse("No report template available for this subject yet.", status=400)

    buffer = gen.generate(teacher.subject.id)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'inline; filename="preview.docx"'
    return response


@login_required(login_url='teacher:login')
def generate_report(request, student_id):
    teacher = request.user.teacher
    student = get_object_or_404(Student, pk=student_id)

    marks = Marks.objects.filter(test__teacher=teacher, student=student)
    tests = Tests.objects.filter(teacher=teacher, subject_id=teacher.subject.id)
    gen = ReportGenerator(student, tests, teacher, marks)

    if not gen.has_template(teacher.subject.id):
        return HttpResponse("No report template available for this subject yet.", status=400)

    buffer = gen.generate_pdf(teacher.subject.id)
    template_name = REPORT_TEMPLATES[teacher.subject.id].replace('.docx', '')
    filename = f"{student.name}_{student.surname}_{template_name}.pdf"

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@login_required(login_url='teacher:login')
def generate_all(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)
    tests    = Tests.objects.filter(teacher=teacher, subject_id=teacher.subject.id)

    if not students.exists():
        return HttpResponse("No students to generate reports for.", status=400)

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for student in students:
            marks = Marks.objects.filter(test__teacher=teacher, student=student)
            gen = ReportGenerator(student, tests, teacher, marks)

            if not gen.has_template(teacher.subject.id):
                return HttpResponse("No report template available for this subject yet.", status=400)

            pdf = gen.generate_pdf(teacher.subject.id)   # same call as generate_report
            if hasattr(pdf, 'getvalue'):
                pdf = pdf.getvalue()

            name = get_valid_filename(f"{student.surname}_{student.name}_{student.exam_num}.pdf")
            zf.writestr(name, pdf)

    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{get_valid_filename(teacher.subject.subject)}_reports.zip"'
    return response

