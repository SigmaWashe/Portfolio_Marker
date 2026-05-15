from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST

from portfolio_marker.models import Subject
from portfolio_marker.models import Student
from core.calculator import calculate_percentage, assign_symbol, round_decimal
from core.constants import BusinessTest, BusinessWeight

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("❌ FORM ERRORS:", form.errors.as_data())
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logins(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            logins(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logouts(request):
    logouts(request)
    return redirect('login')

def business(request):
    return render(request, 'business/business.html')

@login_required
@require_POST
def business_insert(request):
    exam_number = int(request.POST['exam_number'])
    test_id = int(request.POST['test_id'])
    desc = request.POST['desc']
    mark = float(request.POST['mark'])
    total = int(request.POST['total'])

    percentage = calculate_percentage(mark, total)

    match test_id:
        case BusinessTest.TASK: weighted = percentage * BusinessWeight.TASK
        case BusinessTest.SECTION_AB: weighted = percentage * BusinessWeight.SECTION
        case BusinessTest.SECTION_C: weighted = percentage * BusinessWeight.SECTION
        case BusinessTest.PRELIM: weighted = percentage * BusinessWeight.PRELIM
        case _: weighted = 0.0

    student = Student.objects.get(exam_num=exam_number)

    Subject.objects.create(exam_num=student, test_description=desc, actual_mark=mark, possible_mark=total,
                           weighted_mark=round_decimal(weighted, 2), percentage=round_decimal(percentage, 2),
                           symbol=assign_symbol(percentage), submission_date=timezone.now().date(),)
    return redirect('business', exam_number=exam_number)

@login_required
@require_POST
def business_delete(request):
    exam_number = int(request.POST['exam_number'])
    record_id = int(request.POST['id'])
    Subject.objects.filter(exam_num__exam_num=exam_number, subject_id=record_id).delete()
    return redirect('business', exam_number=exam_number)