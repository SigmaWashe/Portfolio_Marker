from django import forms
from django.contrib.auth.forms import UserCreationForm

from student.models import *
from common.models import *
from core.subjects import *

class SignupForm(UserCreationForm):
    exam_num = forms.IntegerField(max_value=999999999999)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['exam_num', 'name', 'surname', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = str(self.cleaned_data['exam_num'])
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        if commit:
            user.save()
            Student.objects.create(user=user, exam_num=self.cleaned_data['exam_num'], name=self.cleaned_data['name'],
                                   surname=self.cleaned_data['surname'],)
        return user


class SubjectForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.none(), required=False, label="Subjects",
                                              widget=forms.SelectMultiple(attrs={'class': 'searchable-select'}),)

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)
        if student:
            field = self.fields['subjects']
            field.queryset = Subject.objects.all()
            field.label_from_instance = lambda obj: obj.subject
            # pre-select the student's current subjects
            self.initial.setdefault('subjects', list(student.subjects.values_list('pk', flat=True)),)


class UpdateTests(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['type', 'description', 'mark', 'total', 'date', ]
        widgets = {
            'date'       : forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'type'       : forms.Select(attrs={'class': 'searchable-select'}),
            'mark'       : forms.NumberInput(attrs={'placeholder': 'e.g., 50'}),
            'total'      : forms.NumberInput(attrs={'placeholder': 'e.g., 100'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g., Literary Essay'}),
        }

    def __init__(self, *args, **kwargs):
        subject = kwargs.pop('subject', None)
        super().__init__(*args, **kwargs)

        test_types = SUBJECT_CHOICES.get(subject)
        choices = [(c[0], c[1]) for c in test_types["choices"]] if test_types else []

        self.fields['type'] = forms.TypedChoiceField(choices=choices, coerce=int,
                                                     widget=forms.Select(attrs={'class': 'searchable-select'}),)

        if self.instance.pk:
            self.initial['type'] = self.instance.type

