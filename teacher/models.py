from django.db import models
from django.contrib.auth.models import User
from core.constants import SubjectID as SubID


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    school = models.ForeignKey('Schools', on_delete=models.CASCADE, related_name='teachers')
    subject = models.ForeignKey('Subject', editable=True, on_delete=models.CASCADE, related_name='teachers')

    class Meta:
        unique_together = ('email', 'name', 'surname')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam_num = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    school = models.ForeignKey('Schools', on_delete=models.CASCADE, related_name='students')

    class Meta:
        unique_together = ('exam_num', 'name', 'surname')


class SubjectID(models.IntegerChoices):
    ACCOUNTING =             SubID.Accounting,             'Accounting'
    AGRICULTURE_MANAGEMENT = SubID.AgriculturalManagement, 'Agricultural Management'
    AGRICULTURE_SCIENCES =   SubID.AgriculturalSciences,   'Agricultural Sciences'
    BUSINESS =               SubID.Business,               'Business Studies'
    CAT =                    SubID.CAT,                    'Computer Applications Technology'
    DESIGN =                 SubID.Design,                 'Design'
    DRAMA =                  SubID.DramaticArts,           'Dramatic Arts'
    ECONOMICS =              SubID.Economics,              'Economics'
    ENG_HL =                 SubID.EngHL,                  'English Home Language'
    FAL =                    SubID.FAL,                    'First Additional Language'
    GEOGRAPHY =              SubID.Geography,              'Geography'
    HISTORY =                SubID.History,                'History'
    INFORMATION_TECHNOLOGY = SubID.IT,                     'Information Technology'
    LIFE_SCIENCES =          SubID.LifeSciences,           'Life Sciences'
    MATHEMATICS =            SubID.Mathematics,            'Mathematics'
    PHYSICAL_SCIENCES =      SubID.PhysicalSciences,       'Physical Sciences'
    VISUAL_ARTS =            SubID.VisualArts,             'Visual Arts'
    OTHER_HL =               SubID.OtherHL,                'Other Home Language'
    LIFE_ORIENTATION =       SubID.LifeOrientation,        'Life Orientation'
    MATHS_LIT =              SubID.MathsLit,               'Mathematical Literacy'


class Subject(models.Model):
    id = models.IntegerField(primary_key=True, choices=SubjectID.choices)
    subject = models.CharField(max_length=100)


class Test(models.Model):
    test_id = models.AutoField(primary_key=True, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    student = models.ForeignKey('Student', editable=False, on_delete=models.CASCADE, related_name='tests')
    test_type = models.IntegerField(default=1)
    test_description = models.CharField(max_length=255)
    actual_mark = models.FloatField()
    possible_mark = models.IntegerField()
    weighted_mark = models.FloatField()
    percentage = models.FloatField()
    symbol = models.IntegerField()
    submission_date = models.DateField()

    class Meta:
        unique_together = ('subject', 'student', 'test_description', 'actual_mark', 'possible_mark')


class Schools(models.Model):
    center_number = models.IntegerField(unique=True)
    name_of_school = models.CharField(max_length=255)

    class Meta:
        unique_together = ('center_number', 'name_of_school')


class ChosenSubjects(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='chosen_subjects')

    accounting = models.BooleanField(default=False)
    agricultural_management = models.BooleanField(default=False)
    agricultural_sciences = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    cat = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    dramatic_arts = models.BooleanField(default=False)
    economics = models.BooleanField(default=False)
    eng_hl = models.BooleanField(default=False)
    fal = models.BooleanField(default=False)
    geography = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    information_technology = models.BooleanField(default=False)
    life_sciences = models.BooleanField(default=False)
    mathematics = models.BooleanField(default=False)
    physical_sciences = models.BooleanField(default=False)
    visual_arts = models.BooleanField(default=False)
    other_hl = models.BooleanField(default=False)
    life_orientation = models.BooleanField(default=False)
    maths_lit = models.BooleanField(default=False)
