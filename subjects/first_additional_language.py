from core.calculator import calculate_percentage, round_decimal
from core.constants import FAL


def build_data(g):
    ext1 = g._mark(FAL.EXT_WRITING, 0)
    ext2 = g._mark(FAL.EXT_WRITING, 1)

    cat = g._mark(FAL.CAT)
    lit = g._mark(FAL.LITERATURE)
    lit_total = g._total(FAL.LITERATURE)

    t1 = g._mark(FAL.TEST, 0)
    t2 = g._mark(FAL.TEST, 1)
    t3 = g._mark(FAL.TEST, 2)

    p1 = g._mark(FAL.PRELIM_PAPER_1)
    p1_total = g._total(FAL.PRELIM_PAPER_1)
    p2 = g._mark(FAL.PRELIM_PAPER_2)
    p2_total = g._total(FAL.PRELIM_PAPER_2)

    sec1 = g._weighted(FAL.EXT_WRITING, 0) + g._weighted(FAL.EXT_WRITING, 1)
    sec2  = g._weighted(FAL.CAT, 0)
    sec3  = g._weighted(FAL.LITERATURE, 0)
    sec4  = g._weighted(FAL.TEST, 0) + g._weighted(FAL.TEST, 1) + g._weighted(FAL.TEST, 2)
    sec5  = g._weighted(FAL.PRELIM_PAPER_1, 0) + g._weighted(FAL.PRELIM_PAPER_2, 1)
    total = sec1 + sec2 + sec3 + sec4 + sec5

    exam = str(g.student.exam_num).zfill(13)

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "{ext1_total}": ext1, "{ext1}": ext1, "{ext1_sym}": g._sym(FAL.EXT_WRITING, 0),
        "{ext2_total}": ext2, "{ext2}": ext2, "{ext2_sym}": g._sym(FAL.EXT_WRITING, 1),
        "{sec1}": sec1, "{sec1_sym}": g._sym_val(sec1, 90),

        "{cat_total}": g._total(FAL.CAT), "{cat}": cat, "{cat_sym}": g._sym(FAL.CAT),
        "{sec2}": sec2, "{sec2_sym}": g._sym_val(sec2, 50),

        "{lit_total}": lit_total, "{lit}": lit, "{lit_sym}": g._sym(FAL.LITERATURE),
        "{sec3}": int(sec3), "{sec3_sym}": g._sym_val(sec3, 60),

        "{test1_total}": g._total(FAL.TEST, 0), "{test1}": t1, "{test1_sym}": g._sym(FAL.TEST, 0),
        "{test2_total}": g._total(FAL.TEST, 1), "{test2}": t2, "{test2_sym}": g._sym(FAL.TEST, 1),
        "{test3_total}": g._total(FAL.TEST, 2), "{test3}": t3, "{test3_sym}": g._sym(FAL.TEST, 2),
        "{sec4}": sec4, "{sec4_sym}": g._sym_val(sec4, 60),

        "{prelim_total}": p1_total+p2_total, "{prelim_mark}": p1+p2, "{prelim_sym}": g._sym_val(p1+p2, p1_total+p2_total),
        "{sec5}": sec5, "{sec5_sym}": g._sym_val(sec5, 40),

        "{total}": total, "{total_sym}": g._sym_val(total, 100),
    }