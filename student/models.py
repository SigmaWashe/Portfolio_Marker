from django.db import models
from django.contrib.auth.models import User

from common.models import Subject

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    exam_num = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        unique_together = ('exam_num', 'name', 'surname')


class Test(models.Model):
    student = models.ForeignKey(Student, editable=False, on_delete=models.CASCADE, related_name='student_tests')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='student_tests')
    type = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    mark = models.FloatField()
    total = models.IntegerField()
    weighted = models.FloatField()
    percentage = models.FloatField()
    symbol = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('subject', 'student', 'description', 'mark', 'total')