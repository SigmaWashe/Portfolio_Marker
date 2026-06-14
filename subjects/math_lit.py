from core.constants import MathsLit


def build_data(g):
    test1_weighted = g._weighted(MathsLit.TEST, 0)
    test2_weighted = g._weighted(MathsLit.TEST, 1)
    alt1_weighted = g._weighted(MathsLit.ALT_TASK, 0)
    alt2_weighted = g._weighted(MathsLit.ALT_TASK, 1)
    prelim1_weighted = g._weighted(MathsLit.PRELIM_PAPER_1)
    prelim2_weighted = g._weighted(MathsLit.PRELIM_PAPER_2)

    weighted = lambda x: float(x) if (x != "" and x is not None) else 0.0

    total = (weighted(test1_weighted)+weighted(test2_weighted)+weighted(alt1_weighted)+weighted(alt2_weighted)+
             weighted(prelim1_weighted)+weighted(prelim2_weighted))


    return {
        "{Examination_Number}": g.student.exam_num,
        "{t1_date}": g._date(MathsLit.TEST, 0), "{t1_desc}": g._desc(MathsLit.TEST, 0), "{t1_mark}": g._mark(MathsLit.TEST, 0),
        "{t1_perc}": g._perc(MathsLit.TEST, 0), "{t1_weight}": test1_weighted,

        "{t2_date}": g._date(MathsLit.TEST, 1), "{t2_desc}": g._desc(MathsLit.TEST, 1), "{t2_mark}": g._mark(MathsLit.TEST, 1),
        "{t2_perc}": g._perc(MathsLit.TEST, 1), "{t2_weight}": test2_weighted,

        "{alt1_date}": g._date(MathsLit.ALT_TASK, 0), "{alt1_desc}": g._desc(MathsLit.ALT_TASK, 0), "{alt1_mark}": g._mark(MathsLit.ALT_TASK, 0),
        "{alt1_perc}": g._perc(MathsLit.ALT_TASK, 0), "{alt1_weight}": alt1_weighted,

        "{alt2_date}": g._date(MathsLit.ALT_TASK, 1), "{alt2_desc}": g._desc(MathsLit.ALT_TASK, 1), "{alt2_mark}": g._mark(MathsLit.ALT_TASK, 1),
        "{alt2_perc}": g._perc(MathsLit.ALT_TASK, 1), "{alt2_weight}": alt2_weighted,

        "{p1_date}": g._date(MathsLit.PRELIM_PAPER_1), "{p1_desc}": g._desc(MathsLit.PRELIM_PAPER_1), "{p1_mark}": g._mark(MathsLit.PRELIM_PAPER_1),
        "{p1_perc}": g._perc(MathsLit.PRELIM_PAPER_1), "{p1_weight}": prelim1_weighted,

        "{p2_date}": g._date(MathsLit.PRELIM_PAPER_2), "{p2_desc}": g._desc(MathsLit.PRELIM_PAPER_2), "{p2_mark}": g._mark(MathsLit.PRELIM_PAPER_2),
        "{p2_perc}": g._perc(MathsLit.PRELIM_PAPER_2), "{p2_weight}": prelim2_weighted,

        "{total}": total
    }