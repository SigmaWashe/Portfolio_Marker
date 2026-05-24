from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.http import require_POST

from portfolio_marker.models import Test, Student
from core.calculator import calculate_percentage, assign_symbol, round_decimal
from core.constants import BusinessTest, BusinessWeight
from .forms import SignupForm

SYMBOL_LABELS = {1: 'F', 2: 'E', 3: 'D', 4: 'C', 5: 'B', 6: 'A', 7: 'A+'}

BUSINESS_TEST_CHOICES = [
    (BusinessTest.TASK, 'Task (SBA)'),
    (BusinessTest.SECTION_AB, 'Section A & B (Test)'),
    (BusinessTest.SECTION_C, 'Section C (Test)'),
    (BusinessTest.PRELIM, 'Preliminary Exam'),
]


def _calc_business(test_id, mark, total):
    percentage = calculate_percentage(mark, total)
    match test_id:
        case BusinessTest.TASK:
            weighted = percentage * BusinessWeight.TASK
        case BusinessTest.SECTION_AB:
            weighted = percentage * BusinessWeight.SECTION
        case BusinessTest.SECTION_C: (
            weighted) = percentage * BusinessWeight.SECTION
        case BusinessTest.PRELIM: (
            weighted) = percentage * BusinessWeight.PRELIM
        case _: (
            weighted) = 0.0
    return percentage, weighted


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('select_subjects')
        else:
            print("❌ FORM ERRORS:", form.errors.as_data())
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
    from portfolio_marker.models import Subject
    student = request.user.student

    if request.method == 'POST':
        subject_ids = [int(i) for i in request.POST.getlist('subjects')]
        if len(subject_ids) < 3:
            return render(request, 'select_subjects.html', {
                'subjects': Subject.objects.all(),
                'error': 'Please select at least 3 subjects.'
            })

        student.eng_hl = 1  in subject_ids
        student.other_hl = 2  in subject_ids
        student.fal = 3  in subject_ids
        student.mathematics = 4  in subject_ids
        student.life_orientation = 5  in subject_ids
        student.business = 6  in subject_ids
        student.cat = 7  in subject_ids
        student.geography = 8  in subject_ids
        student.history = 9  in subject_ids
        student.information_technology = 10 in subject_ids
        student.life_sciences = 11 in subject_ids
        student.physical_sciences = 12 in subject_ids
        student.save()
        return redirect('dashboard')

    return render(request, 'select_subjects.html', {
        'subjects': Subject.objects.all(),
    })


@login_required
def complete_profile(request):
    if hasattr(request.user, 'student'):
        return redirect('dashboard')

    if request.method == 'POST':
        exam_number = request.POST.get('exam_number')
        name        = request.POST.get('name')
        surname     = request.POST.get('surname')

        if not exam_number or not name or not surname:
            return render(request, 'account/complete_profile.html', {'error': 'All fields are required.'})

        if Student.objects.filter(exam_num=exam_number).exists():
            return render(request, 'account/complete_profile.html', {'error': 'Exam number already registered.'})

        Student.objects.create(user=request.user, exam_num=exam_number, name=name, surname=surname)
        return redirect('dashboard')

    return render(request, 'account/complete_profile.html')


@login_required
def dashboard(request):
    pass

@login_required
def business(request):
    pass