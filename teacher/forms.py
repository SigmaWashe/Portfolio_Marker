import json

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import F
from django.http import JsonResponse

from teacher.models import Student, Teacher, Tests, Marks
from common.models import Schools, Subject
from core.subjects import SUBJECTS, SUBJECT_FIELDS, SUBJECT_CHOICES
from core.utils import *
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


class UpdateStudents(forms.ModelForm):
    name     = forms.CharField(max_length=255)
    surname  = forms.CharField(max_length=255)
    exam_num = forms.IntegerField(max_value=999999999999)

    class Meta:
        model = Student
        fields = ['exam_num', 'name', 'surname']
        widgets = {
            'exam_num': forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'e.g., 250001123456'})),
            'name': forms.TextInput(attrs={'placeholder': 'e.g., John'}),
            'surname': forms.TextInput(attrs={'placeholder': 'e.g., Doe'}),
        }


class UpdateTests(forms.ModelForm):
    class Meta:
        model = Tests
        fields = ['type', 'description', 'total', 'date']
        widgets = {
            'date'       : forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'total'      : forms.NumberInput(attrs={'placeholder': 'e.g., 100'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g., Literary Essay'}),
        }

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)

        test_types = SUBJECT_CHOICES.get(teacher.subject_id) if teacher else None
        choices = [(c[0], c[1]) for c in test_types["choices"]] if test_types else []

        self.fields['type'] = forms.TypedChoiceField(choices=choices, coerce=int,
                                                     widget=forms.Select(attrs={'class': 'searchable-select'}),)

        if self.instance.pk:
            self.initial['type']  = self.instance.type
            self.initial['date']  = self.instance.date
            self.initial['total'] = self.instance.total
            self.initial['description'] = self.instance.description


class UpdateMarks(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['mark', 'percentage', 'test']
        widgets = {
            'student'   : forms.TextInput(attrs={'placeholder': 'student', 'readonly': 'readonly'}),
            'mark'      : forms.NumberInput(attrs={'step': '0.5', 'placeholder': 'e.g., 50'}),
            'percentage': forms.NumberInput(attrs={'placeholder': 'auto', 'disabled': 'disabled'}),
            'test'      : forms.Select(attrs={'class': 'searchable-select'}),
        }
        field_order = ['student', 'mark', 'percentage', 'test']

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)

        tests = Tests.objects.filter(teacher=teacher, subject=teacher.subject_id).distinct()
        self.fields['test'].queryset = tests
        self.fields['test'].label_from_instance = lambda obj: f"{obj.test_description}"
        self.fields['percentage'].disabled = True
        self.fields['percentage'].required = False

        if self.instance.pk:
            self.initial['student'] = str(self.instance.student)

        test_pk = self.data.get(self.add_prefix('test')) if self.is_bound else None
        selected = tests.filter(pk=test_pk).first() if test_pk else getattr(self.instance, 'test', None) if self.instance.pk else None

        if selected:
            self.fields['mark'].widget.attrs.update({
                'max': selected.total, 'min': 0, 'placeholder': f'out of {selected.total}',})

        self.fields['test'].widget.attrs['data-totals'] = json.dumps({str(t.pk): t.total for t in tests})

class ManageMarks(forms.Form):
    tests = forms.ModelChoiceField(queryset=Tests.objects.none(), required=True, label="Target assessment",
                                   widget=forms.Select(attrs={'class': 'searchable-select'}))
    total = forms.IntegerField(required=True, label="Out of", min_value=1,
                               widget=forms.NumberInput(attrs={'min': '1', 'placeholder': 'e.g. 100'}))


    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)

        super().__init__(*args, **kwargs)
        if teacher and hasattr(teacher, 'subject'):
            self.fields['tests'].queryset = Tests.objects.filter(teacher=teacher, subject=teacher.subject_id).distinct()
            self.fields['tests'].label_from_instance = lambda obj: f"{obj.description}"


