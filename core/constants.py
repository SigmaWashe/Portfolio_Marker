from core.calculator import *

class SubjectID:
    Accounting = 1
    AgriculturalManagement = 2
    AgriculturalSciences = 3

    Business = 4
    CAT = 5
    Design = 6

    DramaticArts = 7
    Economics = 8
    EngHL = 9

    FAL = 10
    Geography = 11
    History = 12

    IT = 13
    LifeSciences = 14
    Mathematics = 15

    PhysicalSciences = 16
    VisualArts = 17

    OtherHL = 18
    LifeOrientation = 19
    MathsLit = 20
    

class Accounting:
    TEST = 1
    CHOICE_ASSESSMENT_TASK = 2
    PRELIM_PAPER_1 = 3
    PRELIM_PAPER_2 = 4
    CHOICES = [(1, 'Controlled Test', 0.15), (2, 'Choice Assessment Task ', 0.25), (3, 'Prelim Paper 1', 0.15), (4, 'Prelim Paper 2', 0.15)]


class AgriculturalManagement:
    PRELIM_PAPER_1 = 1
    CONTROLLED_TEST = 2
    MANAGEMENT_ASSIGNMENT = 3
    ORAL = 4
    VISUAL = 5
    PRACTICAL = 6
    CHOICES = [(1, 'Paper I', 0.30), (2, 'Controlled Test', 0.15), (3, 'Management Assignment', 0.20), (4, 'Oral Task', 0.10),
               (5, 'Visual Task', 0.10), (6, 'Practical Task', 0.10)]


class AgriculturalSciences:
    PRELIM_PAPER_1 = 1
    CONTROLLED_TEST = 2
    WRITING_PIECE = 3
    ORAL = 4
    VISUAL = 5
    CHOICES = [(1, 'Paper I', 0.30), (2, 'Controlled Test', 0.15), (3, 'Controlled Writing Piece', 0.15), (4, 'Oral Task', 0.15),
               (5, 'Visual Task', 0.15)]


class Business:
    TASK = 1
    SECTION_AB = 2
    SECTION_C = 3
    PRELIM = 4
    CHOICES = [(1, 'Task (SBA)', 0.20), (2, 'Section A & B (Test)', 0.15), (3, 'Section C (Test)', 0.15), (4, 'Preliminary Exam', 0.30),]


class CAT:
    THEORY = 1
    PRAC = 2
    ALT_TEST = 3
    PRELIM_1 = 4
    PRELIM_2 = 5
    PAT = 6
    CHOICES = [(1, 'Theory', .175), (2, 'Practical', 0.175), (3, 'Alternative Test', 0.15), (4, 'Prelim 1', 0.25),
               (5, 'Prelim 2', 0.25), (6, 'PAT', 1.0),]


class Design:
    CAT = 1
    PRELIM = 2
    SECTION_A = 3
    SECTION_B = 4
    SECTION_C = 5
    CHOICES = [(1, 'Common Assessment Task', 0.50), (2, 'Prelim Theory Examination', 0.15), (3, 'Section A Test', 0.10),
               (4, 'Section C Test', 0.10), (5, 'Section C Test', 0.10)]


class DramaticArts:
    PRACTICAL = 1
    THEORY = 2
    PRELIM = 3
    PAT_SECTION_A = 4
    PAT_SECTION_B = 5
    CHOICES = [(1, 'Practical Tasks', 0.25*(5/6)), (2, 'Theoretical Assessment', 0.10*(5/6)),
               (3, 'Prelim', 0.25*(5/6)), (4, 'Section A (PAT)', 0.4*(3/6)), (5, 'Section 2 (PAT)', 0.4*(3/6))]


class Economics:
    PRELIM = 1
    CONTROLLED_TEST = 2
    MULTIPLE_CHOICE = 3
    DATA_RESPONSE = 4
    ORAL = 5
    CHOICES = [(1, 'Prelim Exam', 0.30), (2, 'Controlled Test', 0.25), (3, 'Multiple-Choice Controlled Test', 0.10),
               (4, 'Data Response Task', 0.15), (5, 'Oral presentation', 0.20)]


class EngHL:
    EXT_WRITING = 1
    CAT = 2
    LITERATURE = 3
    TEST = 4
    PRELIM_PAPER_1 = 5
    PRELIM_PAPER_2 = 6
    CHOICES = [(1, 'Extended Writing', 0.15), (2, 'CAT', 0.50/3), (3, 'Literature', 0.20), (4, 'Test', 0.20/3),
               (5, 'Prelim Paper 1', 0.40/3), (6, 'Prelim Paper 2', 0.40/3),]


class FAL:
    EXT_WRITING = 1
    CAT = 2
    LITERATURE = 3
    TEST = 4
    PRELIM_PAPER_1 = 5
    PRELIM_PAPER_2 = 6
    CHOICES = [(1, 'Extended Writing', 0.15), (2, 'CAT', 0.20), (3, 'Literature', 0.20), (4, 'Test', 0.1/3),
               (5, 'Prelim Paper 1', 0.20), (6, 'Prelim Paper 2', 0.20),]


class Geography:
    TASK = 1
    RESEARCH = 2
    TEST = 3
    PRELIM_PAPER_1 = 4
    PRELIM_PAPER_2 = 5
    CHOICES = [(1, 'Task', 0.15), (2, 'Research', 0.30), (3, 'Test', 0.15), (4, 'Prelim Paper 1', 0.125), (5, 'Prelim Paper 2', 0.125),]


class History:
    TEST = 1
    PRELIM_PAPER_1 = 2
    PRELIM_PAPER_2 = 3
    HIST_INV = 4
    SOURCE_ANALYSIS = 5
    SOURCE_BASED_ESSAY = 6
    VISUAL_ANALYSIS = 7
    CHOICES = [(1, 'Test', 0.10), (2, 'Prelim Paper 1', 0.25), (3, 'Prelim Paper 2', 0.25), (4, 'Historical Investigation', 0.45),
               (5, 'Source Analysis', 0.15), (6, 'Source Based Essay', 0.15), (7, 'Visual Analysis', 0.15),]


class IT:
    PAT = 1
    THEORY = 2
    PRAC = 3
    ALT = 4
    PRELIM_THEORY = 5
    PRELIM_PRAC = 6
    CHOICES = [(1, 'PAT', 1.0), (2, 'Theory', 0.175), (3, 'Practical', 0.175), (4, 'Alternative', 0.15),
               (5, 'Prelim Theory', 0.25), (6, 'Prelim Practical', 0.25),]


class LifeOrientation:
    CAT_A_PART_1 = 1
    CAT_A_PART_2 = 2
    PE = 3
    COMMUNITY_SERVICE = 4
    TASK_1 = 5
    TASK_2 = 6
    CHOICES = [(1, 'CAT A Part 1', 1.0), (2, 'CAT A Part 2', 1.0), (3, 'Physical Education', 1.0),
               (4, 'Community Service', 1.0), (5, 'Task 1', 1.0), (6, 'Task 2', 1.0),]


class LifeSciences:
    PRELIM_PAPER_1 = 1
    PRELIM_PAPER_2 = 2
    TEST = 3
    PRAC = 4
    RESEARCH_PROJECT = 5
    CONTROLLED_WRITING_PIECE = 6
    CASE_STUDY = 7
    SUMMATIVE_PRACTICAL = 8
    CHOICES = [(1, 'Prelim Paper 1', 0.25), (2, 'Prelim Paper 2', 0.25), (3, 'Test', 0.15), (4, 'Practical', 0.15),
               (5, 'Research Project', 0.15), (6, 'Controlled Writing Piece', 0.15), (7, 'Case Study', 0.15), (8, 'Summative Practical', 0.15),]


class Mathematics:
    SHORT_ITEM = 1
    LONG_ITEM = 2
    TEST = 3
    PRELIM_PAPER_1 = 4
    PRELIM_PAPER_2 = 5
    CHOICES = [(1, 'Short Item', 0.15), (2, 'Long Item', 0.30), (3, 'Test', 0.10), (4, 'Prelim Paper 1', 0.20), (5, 'Prelim Paper 2', 0.20),]


class PhysicalSciences:
    PHYS_PRAC = 1
    CHEM_PRAC = 2
    PHYS_TEST = 3
    CHEM_TEST = 4
    PRELIM_1 = 5
    PRELIM_2 = 6
    CHOICES = [(1, 'Physics Practical', 0.15), (2, 'Chemistry Practical', 0.15), (3, 'Physics Test', 0.15),
               (4, 'Chemistry Test', 0.15), (5, 'Prelim Paper 1', 0.20), (6, 'Prelim Paper 2', 0.20),]


class VisualArt:

    CHOICES = []
    pass


class OtherHL:
    EXT_WRITING = 1
    CAT_TASK_1 = 2
    CAT_TASK_2 = 3
    LITERATURE = 4
    TEST = 5
    PRELIM_PAPER_1 = 6
    PRELIM_PAPER_2 = 7
    CHOICES = [(1, 'Extended Writing', 0.10), (2, 'CAT Task 1', 0.10), (3, 'CAT Task 2', 0.10), (4, 'Literature', 0.20),
               (5, 'Test', 0.025), (6, 'Prelim Paper 1', 0.20), (7, 'Prelim Paper 2', 0.20),]


class MathsLit:
    TEST = 1
    ALT_TASK = 2
    PRELIM_PAPER_1 = 3
    PRELIM_PAPER_2 = 4
    CHOICES = [(1, 'Test', 0.15), (2, 'Alternate Task', 0.15), (3, 'Examination – Paper 1', 0.20), (4, 'Examination – Paper 2', 0.20),]


#class

