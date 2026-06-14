from core.constants import AgriculturalManagement as AGM
from core.utils import *

def build_data(g):
    center_num = get_center_number(g.student.exam_num)

    prelim_mark = g._mark(AGM.PRELIM_PAPER_1)
    prelim_weighted = g._weighted(AGM.PRELIM_PAPER_1)

    t1_weighted = g._weighted(AGM.CONTROLLED_TEST, 0)
    t2_weighted = g._weighted(AGM.CONTROLLED_TEST, 1)
    management_weighted = g._weighted(AGM.MANAGEMENT_ASSIGNMENT)

    oral_weighted = g._weighted(AGM.ORAL)
    vis_weighted  = g._weighted(AGM.VISUAL)
    prac_weighted = g._weighted(AGM.PRACTICAL)

    return  {
        "{CENTER_NUM}": center_num, "EXAM_NUM": g.student.exam_num,
        "{prelim_date}": g._date(AGM.PRELIM_PAPER_1), "{prelim_mark}": prelim_mark, "{prelim_weight}": prelim_weighted,

        "{t1_topic}": g._desc(AGM.CONTROLLED_TEST), "{t1_date}": g._date(AGM.CONTROLLED_TEST), "{t1_total}": g._total(AGM.CONTROLLED_TEST, 0),
        "{t1_mark}": g._mark(AGM.CONTROLLED_TEST, 0), "{t1_weight}": t1_weighted,

        "{t2_topic}": g._desc(AGM.CONTROLLED_TEST), "{t2_date}": g._date(AGM.CONTROLLED_TEST), "{t2_total}": g._total(AGM.CONTROLLED_TEST, 1),
        "{t2_mark}": g._mark(AGM.CONTROLLED_TEST, 1), "{t2_weight}": t2_weighted,

        "{manage_topic}": g._desc(AGM.MANAGEMENT_ASSIGNMENT), "{manage_date}": g._date(AGM.MANAGEMENT_ASSIGNMENT), "{manage_total}": g._total(AGM.MANAGEMENT_ASSIGNMENT),
        "{manage_mark}": g._mark(AGM.MANAGEMENT_ASSIGNMENT), "{manage_weight}": management_weighted,

        "{oral_topic}": g._desc(AGM.ORAL), "{oral_date}": g._date(AGM.ORAL), "{oral_total}": g._total(AGM.ORAL),
        "{oral_mark}": g._mark(AGM.ORAL), "{oral_weight}": oral_weighted,

        "{visual_topic}": g._desc(AGM.VISUAL), "{visual_date}": g._date(AGM.VISUAL), "{visual_total}": g._total(AGM.VISUAL),
        "{visual_mark}": g._mark(AGM.VISUAL), "{visual_weight}": vis_weighted,

        "{prac_topic}": g._desc(AGM.PRACTICAL), "{prac_date}": g._date(AGM.PRACTICAL), "{prac_total}": g._total(AGM.PRACTICAL),
        "{prac_mark}": g._mark(AGM.PRACTICAL), "{prac_weight}": prac_weighted,

        "{total}": prelim_weighted + t1_weighted + t2_weighted + management_weighted + oral_weighted + vis_weighted + prac_weighted,
    }