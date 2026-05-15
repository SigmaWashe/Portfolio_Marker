from django.db import models
from django.conf import settings

class Student(models.Model):
    exam_num = models.BigIntegerField(primary_key=True, unique=True, editable=False)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        unique_together = ('exam_num', 'name', 'surname')