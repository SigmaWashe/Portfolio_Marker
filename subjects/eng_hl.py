from core.calculator import calculate_percentage, round_decimal
from core.constants import EngHL


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

    sec1  = round_decimal(ext1 + ext2, 2)
    sec2  = round_decimal(cat, 2)
    sec3  = round_decimal(calculate_percentage(lit, lit_total) * 0.6, 2) if lit_total else 0
    sec4  = round_decimal(t1 + t2 + t3, 2)
    prep  = round_decimal(p1 + p2, 2)
    sec5  = round_decimal(calculate_percentage(prep, 200) * 0.4, 2)
    total = round_decimal((sec1 + sec2 + sec3 + sec4 + sec5) / 3, 2)

    exam = str(g.student.exam_num).zfill(13)

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "{ext1}": ext1, "{ext1_sym}": g._sym(EngHL.EXT_WRITING, 0),
        "{ext2}": ext2, "{ext2_sym}": g._sym(EngHL.EXT_WRITING, 1),
        "{sec1}": sec1, "{sec1_sym}": g._sym_val(sec1, 90),

        "{cat}": cat,   "{cat_sym}":  g._sym(EngHL.CAT),
        "{sec2}": sec2, "{sec2_sym}": g._sym_val(sec2, 50),

        "{lit}": lit, "{lit_total}": lit_total, "{lit_sym}": g._sym(EngHL.LITERATURE),
        "{sec3}": int(sec3), "{sec3_sym}": g._sym_val(sec3, 60),

        "{test1}": t1, "{test1_sym}": g._sym(EngHL.TEST, 0),
        "{test2}": t2, "{test2_sym}": g._sym(EngHL.TEST, 1),
        "{test3}": t3, "{test3_sym}": g._sym(EngHL.TEST, 2),
        "{sec4}": sec4, "{sec4_sym}": g._sym_val(sec4, 60),

        "{prep}": prep, "{prep_sym}": g._sym_val(prep, 200),
        "{sec5}": sec5, "{sec5_sym}": g._sym_val(sec5, 40),

        "{total}": total, "{total_sym}": g._sym_val(total, 100),
    }
