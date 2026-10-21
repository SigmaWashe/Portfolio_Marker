from django.db import models
from core.constants import SubjectID as SubID


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

class Schools(models.Model):
    center_number = models.IntegerField(unique=True)
    name_of_school = models.CharField(max_length=255)

    class Meta:
        unique_together = ('center_number', 'name_of_school')

