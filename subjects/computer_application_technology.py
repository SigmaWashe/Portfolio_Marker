from core.calculator import round_decimal
from core.constants import CAT
from core.utils import get_center_number


def build_data(subject):
    theory_mark = subject._mark(CAT.THEORY)
    theory_total = subject._total(CAT.THEORY)
    prac_mark = subject._mark(CAT.PRAC)
    prac_total = subject._total(CAT.PRAC)
    alt_mark = subject._mark(CAT.ALT_TEST)
    alt_total = subject._total(CAT.ALT_TEST)
    p1_mark = subject._mark(CAT.PRELIM_1)
    p2_mark = subject._mark(CAT.PRELIM_2)
    pat_mark = subject._mark(CAT.PAT)

    theory_weighted  = subject._weighted(CAT.THEORY)
    prac_weighted = subject._weighted(CAT.PRAC)
    alt_weighted = subject._weighted(CAT.ALT_TEST)
    prelim1_weighted = subject._weighted(CAT.PRELIM_1)
    prelim2_weighted = subject._weighted(CAT.PRELIM_2)
    pat_weighted = subject._weighted(CAT.PAT)

    sba_total = round_decimal(theory_weighted + prac_weighted + alt_weighted + prelim1_weighted + prelim2_weighted, 2)
    total = round_decimal(sba_total + pat_weighted, 2)

    exam = subject.student.exam_num

    return {
        "{CENTER_NUM}": get_center_number(exam), "{EXAM_NUM}": int(exam),

        "{theory_date}": subject._date(CAT.THEORY), "{theory_desc}": subject._desc(CAT.THEORY), "{theory_mark}": theory_mark,
        "{theory_total}": theory_total, "{theory_weight}": theory_weighted,

        "{prac_date}": subject._date(CAT.PRAC), "{prac_desc}": subject._desc(CAT.PRAC), "{prac_mark}": prac_mark,
        "{prac_total}": prac_total, "{prac_weight}": prac_weighted,

        "{alt_date}": subject._date(CAT.ALT_TEST), "{alt_desc}": subject._desc(CAT.ALT_TEST), "{alt_mark}": alt_mark,
        "{alt_total}": alt_total, "{alt_weight}": alt_weighted,

        "{prelim1_date}": subject._date(CAT.PRELIM_1), "{prelim1_desc}": subject._desc(CAT.PRELIM_1),
        "{prelim1_mark}": p1_mark, "{prelim1_weight}": prelim1_weighted,

        "{prelim2_date}": subject._date(CAT.PRELIM_2), "{prelim2_desc}": subject._desc(CAT.PRELIM_2),
        "{prelim2_mark}": p2_mark, "{prelim2_weight}": prelim2_weighted,

        "{sba_total}": sba_total, "{total}": total,

        "{pat_date}": subject._date(CAT.PAT), "{pat_desc}": subject._desc(CAT.PAT),
        "{pat_mark}": pat_mark, "{pat_weight}": pat_weighted,
    }