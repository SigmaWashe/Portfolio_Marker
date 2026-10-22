from core.utils import get_center_number
from core.constants import IT


def build_data(g):
    exam_num = g.student.exam_num
    return {
        "{CENTER_NUM}": get_center_number(exam_num), "{EXAM_NUM}": int(exam_num),

        "{pat_desc}": g._desc(IT.PAT), "{pat_weight}": g._weighted(IT.PAT),
        "{theory_desc}": g._desc(IT.THEORY), "{theory_weight}": g._weighted(IT.THEORY),
        "{prac_desc}": g._desc(IT.PRAC), "{prac_weight}": g._weighted(IT.PRAC),
        "{alt_desc}": g._desc(IT.ALT), "{alt_weight}": g._weighted(IT.ALT),
        "{prelim1_desc}": g._desc(IT.PRELIM_THEORY), "{prelim1_weight}": g._weighted(IT.PRELIM_THEORY),
        "{prelim2_desc}": g._desc(IT.PRELIM_PRAC), "{prelim2_weight}": g._weighted(IT.PRELIM_PRAC),
        "{sba_mark}": g._weighted(IT.PAT) + g._weighted(IT.THEORY) + g._weighted(IT.PRAC) + g._weighted(IT.ALT) +
                    g._weighted(IT.PRELIM_THEORY) + g._weighted(IT.PRELIM_PRAC),
    }