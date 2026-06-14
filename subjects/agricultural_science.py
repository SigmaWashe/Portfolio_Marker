from core.constants import AgriculturalSciences as AGS
from core.utils import *

def build_data(g):
    center_num = get_center_number(g.student.exam_num)

    prelim_mark = g._mark(AGS.PRELIM_PAPER_1)
    prelim_weighted = g._weighted(AGS.PRELIM_PAPER_1)

    t1_weighted = g._weighted(AGS.CONTROLLED_TEST, 0)
    t2_weighted = g._weighted(AGS.CONTROLLED_TEST, 1)

    wp_weighted = g._weighted(AGS.WRITING_PIECE)
    oral_weighted = g._weighted(AGS.ORAL)
    vis_weighted  = g._weighted(AGS.VISUAL)

    return  {
        "{CENTER_NUM}": center_num, "EXAM_NUM": g.student.exam_num,
        "{prelim_date}": g._date(AGS.PRELIM_PAPER_1), "{prelim_mark}": prelim_mark, "{prelim_weight}": prelim_weighted,

        "{t1_topic}": g._desc(AGS.CONTROLLED_TEST), "{t1_date}": g._date(AGS.CONTROLLED_TEST), "{t1_total}": g._total(AGS.CONTROLLED_TEST, 0),
        "{t1_mark}": g._mark(AGS.CONTROLLED_TEST, 0), "{t1_weight}": t1_weighted,

        "{t2_topic}": g._desc(AGS.CONTROLLED_TEST), "{t2_date}": g._date(AGS.CONTROLLED_TEST), "{t2_total}": g._total(AGS.CONTROLLED_TEST, 1),
        "{t2_mark}": g._mark(AGS.CONTROLLED_TEST, 1), "{t2_weight}": t2_weighted,

        "{oral_topic}": g._desc(AGS.ORAL), "{oral_date}": g._date(AGS.ORAL), "{oral_total}": g._total(AGS.ORAL),
        "{oral_mark}": g._mark(AGS.ORAL), "{oral_weight}": oral_weighted,

        "{visual_topic}": g._desc(AGS.VISUAL), "{visual_date}": g._date(AGS.VISUAL), "{visual_total}": g._total(AGS.VISUAL),
        "{visual_mark}": g._mark(AGS.VISUAL), "{visual_weight}": vis_weighted,

        "{wp_topic}": g._desc(AGS.WRITING_PIECE), "{prac_date}": g._date(AGS.WRITING_PIECE), "{prac_total}": g._total(AGS.WRITING_PIECE),
        "{wp_mark}": g._mark(AGS.WRITING_PIECE), "{prac_weight}": wp_weighted,

        "{total}": prelim_weighted + t1_weighted + t2_weighted + oral_weighted + vis_weighted + wp_weighted,
    }