from django.db import models


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True, unique=True, editable=False)
    exam_num = models.ForeignKey('Student', unique=True, editable=False, on_delete=models.CASCADE, related_name='subject' )
    test_description = models.TextField()
    actual_mark = models.FloatField()
    possible_mark = models.IntegerField()
    weighted_mark = models.FloatField()
    percentage = models.FloatField()
    symbol = models.IntegerField()
    submission_date = models.DateField()
    students = models.ManyToManyField('Student', related_name='subjects', blank=True)