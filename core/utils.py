import datetime

from django.db.models import Avg, F

from core.calculator import round_decimal
from teacher.models import Test, Student

def get_center_number(full_token_string) -> int:
    return int(str(full_token_string).strip()[2:-6])

def format_exam_date(date_str: str) -> str:
    if not date_str:
        return ""
    try:
        dt = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return dt.strftime("%d-%m")
    except ValueError:
        return date_str

def student_average(student) -> float:
    result = Test.objects.filter(student=student).aggregate(average=Avg('percentage'))
    average = result['average']

    return round_decimal(average, 1)

def teachers_students(teacher):
    return Student.objects.filter(school_id=teacher.school).order_by('surname', 'name')