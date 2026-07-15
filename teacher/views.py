from functools import total_ordering

from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg, Model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST

from core.subjects import *
from core.utils import *
from core.base import ReportGenerator, REPORT_TEMPLATES
from .forms import *
from .models import Test, Student, Subject, Schools, Teacher


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = form.cleaned_data.get('subject')
            school  = form.cleaned_data.get('school')
            request.session['subject_id'] = subject.id
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
        else:
            print(" FORM ERRORS:", form.errors.as_data())
    else:
        form = SignupForm()
    return render(request, 'teacher/signup.html', {'form': form})


def logins(request):
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
            return redirect('dashboard')
        else:
            return render(request, 'teacher/login.html', {'error': 'Invalid email or password.'})
    return render(request, 'teacher/login.html')


def logouts(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    teacher = request.user.teacher
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
    return render(request, 'teacher/dashboard.html', {
        'teacher': teacher,
        'current_students': current_students,
        'number_students': students.count(),
    })


@login_required
def student(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)
    exam_num = name = surname = tests = None

    if request.method == 'POST':
        form = StudentForm(request.POST, teacher=teacher)
        if form.is_valid():
            selected_student = form.cleaned_data.get('students') or students.first()

            if selected_student:
                exam_num = selected_student.exam_num
                name = selected_student.name
                surname = selected_student.surname
                tests = Test.objects.filter(student=selected_student, teacher=teacher).order_by('submission_date')
    else:
        form = StudentForm(teacher=teacher)

    return render(request, 'teacher/student.html', {
        'teacher'  : teacher,
        'exam_num' : exam_num,
        'full_name': f"{name} {surname}",
        'tests'    : tests,
        'form'     : form,
        'ct_form'  : CreateTestForm(teacher=teacher),
        'test_form': TestForm(teacher=teacher),
        'current_students': students,
    })


@login_required
@require_POST
def create_test(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)
    form     = CreateTestForm(request.POST, teacher=teacher)

    if form.is_valid():
        test_type        = form.cleaned_data['test_type']
        test_description = form.cleaned_data['test_description']
        submission_date  = form.cleaned_data['submission_date']
        possible_mark    = form.cleaned_data['possible_mark']

        Test.objects.bulk_create([
            Test(
                test_type=test_type,
                test_description=test_description,
                actual_mark=0, possible_mark=possible_mark,
                weighted_mark=0, percentage=0,
                symbol=1, submission_date=submission_date,
                student=student, subject=teacher.subject, teacher=teacher,
            )
            for student in students
        ])
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher'         : teacher,
        'form'            : StudentForm(teacher=teacher),
        'ct_form'         : form,
        'test_form'       : TestForm(teacher=teacher),
        'current_students': students,
    })


@login_required
@require_POST
def test_insert(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)
    form     = StudentForm(request.POST, teacher=teacher)

    if form.is_valid():
        selected_student = form.cleaned_data['students']
        selected_test    = form.cleaned_data['tests']
        calc             = SUBJECT_CALC.get(teacher.subject.id)
        mark             = float(request.POST['mark'])
        total            = selected_test.possible_mark
        percentage, weighted = calc(selected_test.test_type, mark, total)

        Test.objects.filter(test_type=selected_test.test_type, test_description=selected_test.test_description,
                            submission_date=selected_test.submission_date, student=selected_student, subject=teacher.subject, teacher=teacher).update(
            actual_mark = mark, possible_mark = total, weighted_mark  = round_decimal(weighted, 2),
            percentage  = round_decimal(percentage, 2), symbol = assign_symbol(percentage),
        )
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher'         : teacher,
        'form'            : form,
        'ct_form'         : CreateTestForm(teacher=teacher),
        'test_form'       : form,
        'current_students': students,
    })


@login_required
@require_POST
def test_insert_all(request):
    teacher  = request.user.teacher
    students = teachers_students(teacher)
    form     = StudentForm(request.POST, teacher=teacher)

    # students field not required for bulk insert
    form.fields['students'].required = False

    if form.is_valid():
        selected_test = form.cleaned_data['tests']
        calc = SUBJECT_CALC.get(teacher.subject.id)
        total = int(request.POST['total'])

        tests = Test.objects.filter(test_type=selected_test.test_type, test_description=selected_test.test_description,
                                    submission_date=selected_test.submission_date, subject=teacher.subject, teacher=teacher)

        for test in tests:
            # Look up the unique mark using the specific student's ID
            mark_key = f'mark_{test.student_id}'

            if mark_key in request.POST and request.POST[mark_key] != '':
                mark = float(request.POST[mark_key])
                percentage, weighted = calc(selected_test.test_type, mark, total)

                test.actual_mark = mark
                test.possible_mark = total
                test.weighted_mark = round_decimal(weighted, 2)
                test.percentage = round_decimal(percentage, 2)
                test.symbol = assign_symbol(percentage)

        Test.objects.bulk_update(tests, ['actual_mark', 'possible_mark', 'weighted_mark', 'percentage', 'symbol'])
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher': teacher,
        'form': form,
        'ct_form': CreateTestForm(teacher=teacher),
        'test_form': form,
        'current_students': [{'id':s.id, 'exam_num':s.exam_num, 'full_name':f"{s.name} {s.surname}", } for s in students],
    })


@login_required
def create_student(request):
    teacher = request.user.teacher

    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            name     = form.cleaned_data['name']
            surname  = form.cleaned_data['surname']
            exam_num = form.cleaned_data['exam_num']
            school   = Schools.objects.filter(center_number=get_center_number(exam_num)).first()

            if Student.objects.filter(exam_num=exam_num).exists():
                form.add_error('exam_num', 'A student with this exam number already exists.')
            else:
                student = Student.objects.create(exam_num=exam_num, name=name, surname=surname, school=school)

                existing_tests = Test.objects.filter(teacher=teacher, subject=teacher.subject).values('test_type', 'test_description', 'possible_mark', 'submission_date').distinct()

                Test.objects.bulk_create([
                    Test(
                        test_type=test['test_type'],
                        test_description=test['test_description'],
                        actual_mark=0, possible_mark=test['possible_mark'],
                        weighted_mark=0, percentage=0,
                        symbol=1, submission_date=test['submission_date'],
                        student=student, subject=teacher.subject, teacher=teacher,
                    )
                    for test in existing_tests
                ])

                return redirect('student')
    else:
        form = CreateStudentForm()

    return render(request, 'teacher/create_student.html', {
        'teacher' : teacher,
        'form'    : form,
        'subjects': Subject.objects.all(),
    })