import datetime
import json

from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Test, Student, Subject, Schools, Teacher, ChosenSubjects
from core.subjects import *
from .forms import CreateTestForm, SignupForm, StudentForm, TestForm, get_students_for_teacher, CreateStudentForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
        else:
            print(" FORM ERRORS:", form.errors.as_data())
    else:
        form = SignupForm()
    return render(request, 'teacher/signup.html', {'form': form})


def logins(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            return redirect("login")
        
    else:
        form = AuthenticationForm()
    return render(request, 'teacher/login.html', {'form': form})


def logouts(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    teacher = request.user.teacher
    students = get_students_for_teacher(teacher)
    current_students = [
        {
            'id'  : student.id,
            'name': student.user.get_full_name(),
            'slug': student.user.get_full_name().lower().replace('-', ' '),
        }
        for student in students
    ]
    return render(request, 'teacher/dashboard.html', {
        'teacher': teacher,
        'current_students': current_students,
    })


@login_required
def student(request):
    teacher = request.user.teacher
    exam_num = None
    name = None
    surname = None
    tests = None

    if request.method == 'POST':
        form = StudentForm(request.POST, teacher=teacher)
        if form.is_valid():
            selected_student = form.cleaned_data['students']
            exam_num = selected_student.exam_number
            name     = selected_student.user.first_name
            surname  = selected_student.user.last_name
            tests    = Test.objects.filter(student=selected_student, subject=teacher.subject).order_by('submission_date')
            for test in tests:
                test.symbol_info = assign_symbol(test.percentage, as_dict=True)
    else:
        form = StudentForm(teacher=teacher)

    return render(request, 'teacher/student.html', {
        'teacher'    : teacher,
        'exam_num'   : exam_num,
        'name'       : name,
        'surname'    : surname,
        'tests'      : tests,
        'form'       : form,
        'ct_form'    : CreateTestForm(teacher=teacher),
        'test_form'  : TestForm(teacher=teacher),
        'current_students': [{'id': s.id, 'name': s.user.get_full_name()} for s in get_students_for_teacher(teacher)],
    })


@login_required
@require_POST
def create_test(request):
    teacher  = request.user.teacher
    students = get_students_for_teacher(teacher)
    form     = CreateTestForm(request.POST, teacher=teacher)

    if form.is_valid():
        test_type_id     = form.cleaned_data['tests_type']
        test_description = form.cleaned_data['test_description']
        submission_date  = form.cleaned_data['submission_date']

        Test.objects.bulk_create([
            Test(
                student=student,
                subject=teacher.subject,
                test_type=test_type_id,
                test_description=test_description,
                actual_mark=0, possible_mark=0,
                weighted_mark=0, percentage=0,
                symbol=1, submission_date=submission_date,
            )
            for student in students
        ])
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher'         : teacher,
        'form'            : StudentForm(teacher=teacher),
        'ct_form'         : form,
        'test_form'       : TestForm(teacher=teacher),
        'current_students': [{'id': s.id, 'name': s.user.get_full_name()} for s in students],
    })


@login_required
@require_POST
def test_insert(request):
    teacher  = request.user.teacher
    students = get_students_for_teacher(teacher)
    form     = StudentForm(request.POST, teacher=teacher)

    if form.is_valid():
        selected_student = form.cleaned_data['students']
        selected_test    = form.cleaned_data['tests']
        calc             = SUBJECT_CALC.get(teacher.subject.id)
        mark             = float(request.POST['mark'])
        total            = int(request.POST['total'])
        percentage, weighted = calc(selected_test.test_type, mark, total)

        Test.objects.create(
            student          = selected_student,
            subject          = teacher.subject,
            test_type        = selected_test.test_type,
            test_description = selected_test.test_description,
            actual_mark      = mark,
            possible_mark    = total,
            weighted_mark    = round_decimal(weighted, 2),
            percentage       = round_decimal(percentage, 2),
            symbol           = assign_symbol(percentage),
            submission_date  = selected_test.submission_date,
        )
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher'         : teacher,
        'form'            : form,
        'ct_form'         : CreateTestForm(teacher=teacher),
        'test_form'       : form,
        'current_students': [{'id': s.id, 'name': s.user.get_full_name()} for s in students],
    })


@login_required
@require_POST
def test_insert_all(request):
    teacher  = request.user.teacher
    students = get_students_for_teacher(teacher)
    form     = StudentForm(request.POST, teacher=teacher)

    # students field not required for bulk insert
    form.fields['students'].required = False

    if form.is_valid():
        selected_test = form.cleaned_data['tests']
        calc          = SUBJECT_CALC.get(teacher.subject.id)
        mark          = float(request.POST['mark'])
        total         = int(request.POST['total'])
        percentage, weighted = calc(selected_test.test_type, mark, total)

        Test.objects.bulk_create([
            Test(
                student          = student,
                subject          = teacher.subject,
                test_type        = selected_test.test_type,
                test_description = selected_test.test_description,
                actual_mark      = mark,
                possible_mark    = total,
                weighted_mark    = round_decimal(weighted, 2),
                percentage       = round_decimal(percentage, 2),
                symbol           = assign_symbol(percentage),
                submission_date  = selected_test.submission_date,
            )
            for student in students
        ])
        return redirect('student')

    return render(request, 'teacher/student.html', {
        'teacher'         : teacher,
        'form'            : form,
        'ct_form'         : CreateTestForm(teacher=teacher),
        'test_form'       : form,
        'current_students': [{'id': s.id, 'name': s.user.get_full_name()} for s in students],
    })


@login_required
def create_student(request):
    teacher = request.user.teacher

    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            email      = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            exam_num   = form.cleaned_data['exam_num']
            password   = form.cleaned_data['password']
            subjects   = form.cleaned_data['subject']

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'A student with this email already exists.')
            elif Student.objects.filter(exam_num=exam_num).exists():
                form.add_error('exam_num', 'A student with this exam number already exists.')
            else:
                user = User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password,)
                student = Student.objects.create(user=user,exam_num=exam_num,name=first_name,surname=last_name,school=teacher.school,)
                chosen = ChosenSubjects.objects.create(student=student)
                for sub in subjects:
                    field = SUBJECT_FIELDS.get(sub.id)
                    if field:
                        setattr(chosen, field, True)
                chosen.save()

                return redirect('student')
    else:
        form = CreateStudentForm()

    return render(request, 'teacher/create_student.html', {
        'teacher': teacher,
        'form': form,
        'subjects': Subject.objects.all(),
    })