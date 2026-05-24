from django.db import models

class SubjectID(models.IntegerChoices):
    ENG_HL = 1, 'English Home Language'
    OTHER_HL = 2, 'Other Home Language'
    FAL = 3, 'First Additional Language'
    MATHEMATICS = 4, 'Mathematics'
    LIFE_ORIENTATION = 5, 'Life Orientation'
    BUSINESS = 6, 'Business Studies'
    CAT = 7, 'Computer Applications Technology'
    GEOGRAPHY = 8, 'Geography'
    HISTORY = 9, 'History'
    INFORMATION_TECHNOLOGY = 10, 'Information Technology'
    LIFE_SCIENCES = 11, 'Life Sciences'
    PHYSICAL_SCIENCES = 12, 'Physical Sciences'

class Subject(models.Model):
    id = models.IntegerField(primary_key=True, choices=SubjectID.choices)
    subject = models.CharField(max_length=100)

class Test(models.Model):
    test_id = models.AutoField(primary_key=True, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    student = models.ForeignKey('Student', editable=False, on_delete=models.CASCADE, related_name='tests')
    test_description = models.TextField()
    actual_mark = models.FloatField()
    possible_mark = models.IntegerField()
    weighted_mark = models.FloatField()
    percentage = models.FloatField()
    symbol = models.IntegerField()
    submission_date = models.DateField()

    class Meta:
        unique_together = ('subject', 'student', 'test_description', 'actual_mark', 'possible_mark')