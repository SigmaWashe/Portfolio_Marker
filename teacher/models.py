from django.db import models
from django.contrib.auth.models import User
from common.models import Subject, Schools


class Teacher(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    school  = models.ForeignKey(Schools, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, editable=True, on_delete=models.CASCADE, related_name='teacher')

    class Meta:
        unique_together = ('email', 'name', 'surname')


class Student(models.Model):
    exam_num = models.BigIntegerField(unique=True)
    name     = models.CharField(max_length=100)
    surname  = models.CharField(max_length=100)
    school   = models.ForeignKey(Schools, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('exam_num', 'name', 'surname')


class Tests(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_tests')
    type = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    total = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('subject', 'teacher', 'description', 'total')


class Marks(models.Model):
    test       = models.ForeignKey(Tests, on_delete=models.CASCADE)
    student    = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks', editable=False)
    symbol     = models.IntegerField(default=1)
    mark       = models.FloatField(default=0)
    weighted   = models.FloatField(default=0)
    percentage = models.FloatField(default=0)

    class Meta:
        unique_together = ('test', 'student')