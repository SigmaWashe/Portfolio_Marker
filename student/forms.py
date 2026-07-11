from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

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