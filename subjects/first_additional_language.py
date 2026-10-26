from core.calculator import calculate_percentage, round_decimal, assign_symbol
from core.constants import FAL
from core.utils import n


def build_data(g):
    ext1 = g._mark(FAL.EXT_WRITING, 0)
    ext1_total = g._total(FAL.EXT_WRITING, 0)
    ext2 = g._mark(FAL.EXT_WRITING, 1)
    ext2_total = g._total(FAL.EXT_WRITING, 1)

    cat = g._mark(FAL.CAT)
    lit = g._mark(FAL.LITERATURE)
    lit_total = g._total(FAL.LITERATURE)

    t1 = g._mark(FAL.TEST, 0)
    t2 = g._mark(FAL.TEST, 1)
    t3 = g._mark(FAL.TEST, 2)

    p1 = n(g._mark(FAL.PRELIM_PAPER_1))
    p1_total = n(g._total(FAL.PRELIM_PAPER_1))
    p2 = n(g._mark(FAL.PRELIM_PAPER_2))
    p2_total = n(g._total(FAL.PRELIM_PAPER_2))

    sec1  = n(g._weighted(FAL.EXT_WRITING, 0)) + n(g._weighted(FAL.EXT_WRITING, 1))
    sec2  = n(g._weighted(FAL.CAT, 0))
    sec3  = n(g._weighted(FAL.LITERATURE, 0))
    sec4  = n(g._weighted(FAL.TEST, 0)) + n(g._weighted(FAL.TEST, 1)) + n(g._weighted(FAL.TEST, 2))
    sec5  = n(g._weighted(FAL.PRELIM_PAPER_1, 0)) + n(g._weighted(FAL.PRELIM_PAPER_2, 1))
    total = sec1 + sec2 + sec3 + sec4 + sec5

    exam_num = f"{g.student.exam_num} "

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam_num[0], "{2}": exam_num[1], "{3}": exam_num[2], "{4}": exam_num[3],
        "{5}": exam_num[4], "{6}": exam_num[5], "{7}": exam_num[6], "{8}": exam_num[7],
        "{9}": exam_num[8], "{10}": exam_num[9], "{11}": exam_num[10], "{12}": exam_num[11], "{13}": exam_num[12],

        "{ext1_total}": ext1_total, "{ext1}": ext1, "{ext1_sym}": assign_symbol(n(g._perc(FAL.EXT_WRITING, 0))),
        "{ext2_total}": ext2_total, "{ext2}": ext2, "{ext2_sym}": assign_symbol(n(g._perc(FAL.EXT_WRITING, 1))),
        "{sec1}": sec1, "{sec1_sym}": assign_symbol(calculate_percentage(sec1, 30)),

        "{cat_total}": g._total(FAL.CAT), "{cat}": cat, "{cat_sym}": g._weighted(FAL.CAT),
        "{sec2}": sec2, "{sec2_sym}": assign_symbol(calculate_percentage(sec2, 20)),

        "{lit_total}": lit_total, "{lit}": lit, "{lit_sym}": g._weighted(FAL.LITERATURE),
        "{sec3}": int(sec3), "{sec3_sym}": assign_symbol(calculate_percentage(sec3, 20)),

        "{test1_total}": g._total(FAL.TEST, 0), "{test1}": t1, "{test1_sym}": assign_symbol(n(g._perc(FAL.TEST, 0))),
        "{test2_total}": g._total(FAL.TEST, 1), "{test2}": t2, "{test2_sym}": assign_symbol(n(g._perc(FAL.TEST, 1))),
        "{test3_total}": g._total(FAL.TEST, 2), "{test3}": t3, "{test3_sym}": assign_symbol(n(g._perc(FAL.TEST, 2))),
        "{sec4}": sec4, "{sec4_sym}": assign_symbol(calculate_percentage(sec4, 10)),

        "{prelim_total}": p1_total+p2_total, "{prelim_mark}": p1+p2, "{prelim_sym}": assign_symbol(calculate_percentage(p1+p2, p1_total+p2_total)),
        "{sec5}": sec5, "{sec5_sym}": assign_symbol(calculate_percentage(sec5, 20)),

        "{total}": total, "{total_sym}": assign_symbol(calculate_percentage(total, 100)),
    }