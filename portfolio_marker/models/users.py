from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam_num = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    # Subjects
    eng_hl = models.BooleanField(default=False)
    other_hl = models.BooleanField(default=False)
    fal = models.BooleanField(default=False)
    mathematics = models.BooleanField(default=False)
    life_orientation = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    cat = models.BooleanField(default=False)
    geography = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    information_technology = models.BooleanField(default=False)
    life_sciences = models.BooleanField(default=False)
    physical_sciences = models.BooleanField(default=False)

    class Meta:
        unique_together = ('exam_num', 'name', 'surname')