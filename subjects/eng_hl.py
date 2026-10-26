from core import assign_symbol
from core.calculator import calculate_percentage, round_decimal
from core.constants import EngHL
from core.utils import n


def build_data(g):
    ext1 = g._mark(EngHL.EXT_WRITING, 0)
    ext2 = g._mark(EngHL.EXT_WRITING, 1)

    cat = g._mark(EngHL.CAT)
    lit = g._mark(EngHL.LITERATURE)
    lit_total = g._total(EngHL.LITERATURE)

    t1 = g._mark(EngHL.TEST, 0)
    t2 = g._mark(EngHL.TEST, 1)
    t3 = g._mark(EngHL.TEST, 2)

    p1 = g._mark(EngHL.PRELIM_PAPER_1)
    p2 = g._mark(EngHL.PRELIM_PAPER_2)

    sec1  = round_decimal(n(ext1) + n(ext2), 2)
    sec2  = round_decimal(n(cat), 2)
    sec3  = round_decimal(calculate_percentage(n(lit), n(lit_total)) * 0.6, 2) if lit_total else 0
    sec4  = round_decimal(n(t1) + n(t2) + n(t3), 2)
    prep  = round_decimal(n(p1) + n(p2), 2)
    sec5  = round_decimal(calculate_percentage(prep, 200) * 0.4, 2)
    total = round_decimal((sec1 + sec2 + sec3 + sec4 + sec5) / 3, 2)

    exam_num = f"{g.student.exam_num} "

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam_num[0], "{2}": exam_num[1], "{3}": exam_num[2], "{4}": exam_num[3],
        "{5}": exam_num[4], "{6}": exam_num[5], "{7}": exam_num[6], "{8}": exam_num[7],
        "{9}": exam_num[8], "{10}": exam_num[9], "{11}": exam_num[10], "{12}": exam_num[11], "{13}": exam_num[12],

        "{ext1}": ext1, "{ext1_sym}": assign_symbol(n(g._perc(EngHL.EXT_WRITING, 0))),
        "{ext2}": ext2, "{ext2_sym}": assign_symbol(n(g._perc(EngHL.EXT_WRITING, 1))),
        "{sec1}": sec1, "{sec1_sym}": assign_symbol(calculate_percentage(sec1, 90)),

        "{cat}": cat,   "{cat_sym}": assign_symbol(n(g._perc(EngHL.CAT))),
        "{sec2}": sec2, "{sec2_sym}": assign_symbol(calculate_percentage(sec2, 50)),

        "{lit}": lit, "{lit_total}": lit_total, "{lit_sym}": assign_symbol(n(g._perc(EngHL.LITERATURE))),
        "{sec3}": int(sec3), "{sec3_sym}": assign_symbol(calculate_percentage(sec3, 60)),

        "{test1}": t1, "{test1_sym}": assign_symbol(n(g._perc(EngHL.TEST, 0))),
        "{test2}": t2, "{test2_sym}": assign_symbol(n(g._perc(EngHL.TEST, 1))),
        "{test3}": t3, "{test3_sym}": assign_symbol(n(g._perc(EngHL.TEST, 2))),
        "{sec4}": sec4, "{sec4_sym}": assign_symbol(calculate_percentage(sec4, 60)),

        "{prep}": prep, "{prep_sym}": assign_symbol(calculate_percentage(prep, 200)),
        "{sec5}": sec5, "{sec5_sym}": assign_symbol(calculate_percentage(sec5, 40)),

        "{total}": total, "{total_sym}": assign_symbol(calculate_percentage(total, 100)),
    }
