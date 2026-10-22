from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import F

from .models import Student, Teacher, Test
from student.models import Schools, Subject
from core.subjects import SUBJECTS, SUBJECT_FIELDS
from core.utils import teachers_students
import core.constants


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)

    school = forms.ModelChoiceField(queryset=Schools.objects.all(), required=True, label="Select School",
                                    widget=forms.Select(attrs={'class': 'searchable-select'}))
    
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=True, label="Teaching Subject",
                                     widget=forms.Select(attrs={'class': 'searchable-select'}))

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email   
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['school'].label_from_instance = lambda obj: f"[{obj.center_number}] {obj.name_of_school}"
        self.fields['subject'].label_from_instance = lambda obj: f"{obj.subject}"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        if commit:
            user.save()
            Teacher.objects.create(user=user, email=self.cleaned_data['email'], name=self.cleaned_data['name'],
                                   surname=self.cleaned_data['surname'], school=self.cleaned_data['school'],
                                   subject=self.cleaned_data['subject'])
        return user


"""
def teachers_students(teacher):
    return (Student.objects.filter(teacher_tests__teacher=teacher, school_id=F('teacher_tests__teacher__school_id'))
            .distinct().order_by('surname'))
"""


class StudentForm(forms.Form):
    students = forms.ModelChoiceField(queryset=Student.objects.none(), required=False, label="Students",
                                      widget=forms.Select(attrs={'class': 'searchable-select'}))
    tests = forms.ModelChoiceField(queryset=Test.objects.none(), required=False, label="Select Test",
                                   widget=forms.Select(attrs={'class': 'searchable-select'}))

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)
        if teacher:
            self.fields['students'].queryset = teachers_students(teacher)
            self.fields['students'].label_from_instance = lambda obj: f"{obj.name} {obj.surname} [{obj.exam_num}]"
            self.fields['tests'].queryset = Test.objects.filter(teacher=teacher, subject=teacher.subject).distinct()
            self.fields['tests'].label_from_instance = lambda obj: f"{obj.test_description} total: ({obj.possible_mark})"


class TestForm(forms.Form):
    students = forms.ModelChoiceField(queryset=Student.objects.none(), required=False, label="Students",
                                      widget=forms.Select(attrs={'class': 'searchable-select'}))
    tests = forms.ModelChoiceField(queryset=Test.objects.none(), required=False, label="Select Test",
                                   widget=forms.Select(attrs={'class': 'searchable-select'}))

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)
        if teacher:
            self.fields['students'].queryset = teachers_students(teacher)
            self.fields['students'].label_from_instance = lambda obj: f"[{obj.exam_num}] {obj.name} {obj.surname}"
            self.fields['tests'].queryset = Test.objects.filter(teacher=teacher.id, subject=teacher.subject)
            self.fields['tests'].label_from_instance = lambda obj: f"{obj.test_description} total: ({obj.possible_mark})"


class CreateTestForm(forms.Form):
    test_type        = forms.ChoiceField(required=True, label="Test Type", choices=[], widget=forms.Select(attrs={'class': 'searchable-select'}))
    test_description = forms.CharField(required=True, label="Test Description / Topic", max_length=255)
    submission_date  = forms.DateField(required=True, label="Submission Date", widget=forms.DateInput(attrs={'type': 'date'}))
    possible_mark    = forms.IntegerField(required=True, label="Total", min_value=1, widget=forms.NumberInput(attrs={'type': 'number', 'min': '1'}))

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)
        if teacher and hasattr(teacher, 'subject'):
            subject_name = SUBJECTS.get(teacher.subject.id)
            if subject_name   == "Business Studies"                : class_name = "Business"
            elif subject_name == "Computer Applications Technology": class_name = "CAT"
            elif subject_name == "English Home Language"           : class_name = "EngHL"
            elif subject_name == "First Additional Language"       : class_name = "FAL"
            elif subject_name == "Information Technology"          : class_name = "IT"
            elif subject_name == "Mathematical Literacy"           : class_name = "MathsLit"
            elif subject_name == "Visual Arts"                     : class_name = "VisualArt"
            else: class_name = subject_name.replace(" ", "") if subject_name else ""
            target_class = getattr(core.constants, class_name, None)
            if target_class and hasattr(target_class, 'CHOICES'):
                self.fields['test_type'].choices = [(item[0], item[1]) for item in target_class.CHOICES]


class CreateStudentForm(forms.Form):
    name     = forms.CharField(max_length=255)
    surname  = forms.CharField(max_length=255)
    exam_num = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InsertMarks(forms.Form):
    pass