from core.constants import Design
from core.utils import *


def build_data(g):
    exam_num = g.student.exam_num

    return {
        "{EXAM_NUM}": exam_num, "{CENTER_NUM}": get_center_number(exam_num),
        "{prelim}": g._weighted(Design.PRELIM), "{cat}": g._weighted(Design.CAT), "{sec_A}": g._weighted(Design.SECTION_A),
        "{sec_B}":  g._weighted(Design.SECTION_B), "{sec_C}": g._weighted(Design.SECTION_C),
        "{total}":  n(g._weighted(Design.PRELIM)) + n(g._weighted(Design.CAT)) + n(g._weighted(Design.SECTION_A)) +
                    n(g._weighted(Design.SECTION_B)) + n(g._weighted(Design.SECTION_C))
    }