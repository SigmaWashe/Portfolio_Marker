import datetime
import core.constants
import core.subjects

from django.db.models import Avg, F, Prefetch

from core.calculator import round_decimal
from core.subjects import *
from teacher.models import *

def get_center_number(exam_num):
    exam_num_str = str(exam_num)

    if len(exam_num_str) == 12:   return int(str(exam_num_str).strip()[2:-6])
    elif len(exam_num_str) == 13: return int(str(exam_num_str).strip()[2:-7])

    return 'Invalid exam number'


def format_exam_date(date_str: str) -> str:
    if not date_str:
        return ""
    try:
        return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").strftime("%d-%m")
    except ValueError:
        return date_str


def choices(subject_id):
    test_types = None

    subject_name = core.subjects.SUBJECTS.get(subject_id)

    if subject_name   == "Business Studies":
        class_name = "Business"
    elif subject_name == "Computer Applications Technology":
        class_name = "CAT"
    elif subject_name == "English Home Language":
        class_name = "EngHL"
    elif subject_name == "First Additional Language":
        class_name = "FAL"
    elif subject_name == "Information Technology":
        class_name = "IT"
    elif subject_name == "Mathematical Literacy":
        class_name = "MathsLit"
    elif subject_name == "Visual Arts":
        class_name = "VisualArt"
    elif subject_name == "Other Home Language":
        class_name = "OtherHL"
    else:
        class_name = subject_name.replace(" ", "") if subject_name else ""

    target_class = getattr(core.constants, class_name, None)

    if target_class and hasattr(target_class, 'CHOICES'):
        choices = target_class.CHOICES

        test_types = [{'id': choice[0], 'type': choice[1], 'weighting': choice[2],} for choice in choices]

    return test_types


def test_type(subject_id, type_id):
    types = choices(subject_id) or []

    for choice in types:
        if str(choice['id']) == str(type_id): return choice['type']
    return None


def student_average(student) -> float:
    result = Marks.objects.filter(student=student).aggregate(average=Avg('percentage'))
    average = result['average']
    return round_decimal(average, 1)


def subject_average(teacher):
    result = Marks.objects.filter(test__teacher=teacher,).aggregate(average=Avg('percentage'))
    average = result['average']
    return round_decimal(average, 2)


def test_average(teacher, test):
    result = Marks.objects.filter(test__teacher=teacher, test=test).aggregate(average=Avg('percentage'))
    average = result['average']
    return round_decimal(average, 1)


def teachers_students(teacher): return Student.objects.filter(school=teacher.school).order_by('surname', 'name')


def teachers_tests(teacher): return Tests.objects.filter(teacher=teacher).order_by('-date')


def student_marks(teacher):
    return Marks.objects.filter(test__teacher=teacher).order_by('student__surname', 'student__name', '-test__date')


def n(value): return value or 0
