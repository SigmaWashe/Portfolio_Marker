from core.utils import get_center_number
from core.constants import IT


def build_data(g):
    exam_num = g.student.exam_num
    return {
        "{CENTER_NUM}": get_center_number(exam_num), "{EXAM_NUM}": int(exam_num),

        "pat_desc": g._desc(IT.PAT), "pat_weight": g._weight(IT.PAT),
        "theory_desc": g._desc(IT.THEORY), "theory_weight": g._weight(IT.THEORY),
        "prac_desc": g._desc(IT.PRAC), "prac_weight": g._weight(IT.PRAC),
        "alt_desc": g._desc(IT.ALT), "alt_weight": g._weight(IT.ALT),
        "prelim1_desc": g._desc(IT.PRELIM_THEORY), "prelim1_weight": g._weight(IT.PRELIM_THEORY),
        "prelim2_desc": g._desc(IT.PRELIM_PRAC), "prelim2_weight": g._weight(IT.PRELIM_PRAC),
        "sba_mark": g._weight(IT.PAT) + g._weight(IT.THEORY) + g._weight(IT.PRAC) + g._weight(IT.ALT) +
                    g._weight(IT.PRELIM_THEORY) + g._weight(IT.PRELIM_PRAC),
    }