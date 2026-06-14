from core.calculator import round_decimal, assign_symbol
from core.constants import Mathematics
from core.utils import get_center_number


def build_data(g):
    short1_perc = g._perc(Mathematics.SHORT_ITEM, 0)
    short2_perc = g._perc(Mathematics.SHORT_ITEM, 1)
    long_perc   = g._perc(Mathematics.LONG_ITEM)
    test1_perc  = g._perc(Mathematics.TEST, 0)
    test2_perc  = g._perc(Mathematics.TEST, 1)
    test3_perc  = g._perc(Mathematics.TEST, 2)
    p1_perc     = g._perc(Mathematics.PRELIM_PAPER_1)
    p2_perc     = g._perc(Mathematics.PRELIM_PAPER_2)

    short_weight  = round_decimal(g._weighted(Mathematics.SHORT_ITEM, 0) + g._weighted(Mathematics.SHORT_ITEM, 1), 1)
    long_weight   = g._weighted(Mathematics.LONG_ITEM)
    test_weight   = round_decimal(g._weighted(Mathematics.TEST, 0) + g._weighted(Mathematics.TEST, 1) + g._weighted(Mathematics.TEST, 2), 1)
    prelim_weight = round_decimal(g._weighted(Mathematics.PRELIM_PAPER_1) + g._weighted(Mathematics.PRELIM_PAPER_2), 1)

    short_wins = short_weight >= long_weight
    total = round_decimal((short_weight if short_wins else long_weight) + test_weight + prelim_weight, 1)

    exam = str(g.student.exam_num).zfill(13)

    data = {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "{short1_topic}": g._desc(Mathematics.SHORT_ITEM, 0), "{short1_mark}": g._mark(Mathematics.SHORT_ITEM, 0),
        "{short1_total}": g._total(Mathematics.SHORT_ITEM, 0), "{short1_perc}": short1_perc,

        "{short2_topic}": g._desc(Mathematics.SHORT_ITEM, 1), "{short2_mark}": g._mark(Mathematics.SHORT_ITEM, 1),
        "{short2_total}": g._total(Mathematics.SHORT_ITEM, 1), "{short2_perc}": short2_perc,

        "{short_weight}": short_weight,

        "{long_topic}": g._desc(Mathematics.LONG_ITEM), "{long_mark}": g._mark(Mathematics.LONG_ITEM),
        "{long_total}": g._total(Mathematics.LONG_ITEM), "{long_perc}": long_perc,

        "{long_weight}": long_weight,

        "{test1_topic}": g._desc(Mathematics.TEST, 0), "{test1_mark}": g._mark(Mathematics.TEST, 0),
        "{test1_total}": g._total(Mathematics.TEST, 0), "{test1_perc}": test1_perc,

        "{test2_topic}": g._desc(Mathematics.TEST, 1), "{test2_mark}": g._mark(Mathematics.TEST, 1),
        "{test2_total}": g._total(Mathematics.TEST, 1), "{test2_perc}": test2_perc,

        "{test3_topic}": g._desc(Mathematics.TEST, 2), "{test3_mark}": g._mark(Mathematics.TEST, 2),
        "{test3_total}": g._total(Mathematics.TEST, 2), "{test3_perc}": test3_perc,

        "{test_weight}": test_weight,

        "{prelim1_mark}": g._mark(Mathematics.PRELIM_PAPER_1), "{prelim1_total}": g._total(Mathematics.PRELIM_PAPER_1),
        "{prelim1_perc}": p1_perc,

        "{prelim2_mark}": g._mark(Mathematics.PRELIM_PAPER_2), "{prelim2_total}": g._total(Mathematics.PRELIM_PAPER_2),
        "{prelim2_perc}": p2_perc,

        "{prelim_weight}": prelim_weight,

        "{total}": total, "{total_sym}": assign_symbol(total),
    }

    if short_wins:
        data["{long_topic}"] = data["{long_mark}"] = data["{long_total}"] = data["{long_perc}"] = data["{long_weight}"] = ""
    else:
        data["{short1_topic}"] = data["{short1_mark}"] = data["{short1_total}"] = data["{short1_perc}"] = ""
        data["{short2_topic}"] = data["{short2_mark}"] = data["{short2_total}"] = data["{short2_perc}"] = data["{short_weight}"] = ""

    return data