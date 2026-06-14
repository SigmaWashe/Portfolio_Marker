from core.constants import VisualArt
from core.utils import *


def build_data(g):
    return {
        "{EXAM_NUMBER}": g.student.exam_num, "{CENTER_NUMBER}": get_center_number(g.student.exam_num), "{SCHOOL}": g.student.school,
    }