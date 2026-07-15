from django.db import models
from django.contrib.auth.models import User
from student.models import Subject, Schools


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


class Test(models.Model):
    test_id = models.AutoField(primary_key=True, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teacher_tests')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_tests')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teacher_tests', editable=False)
    test_type = models.IntegerField(default=1)
    test_description = models.CharField(max_length=255)
    actual_mark = models.FloatField()
    possible_mark = models.IntegerField()
    weighted_mark = models.FloatField()
    percentage = models.FloatField()
    symbol = models.IntegerField()
    submission_date = models.DateField()

    class Meta:
        unique_together = ('subject', 'student', 'test_description')
