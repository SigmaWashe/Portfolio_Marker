from core.calculator import assign_symbol
from core.constants import Business


def build_data(g):
    t1_mark     = g._mark(Business.TASK, 0)
    t1_tot      = g._total(Business.TASK, 0)
    t2_mark     = g._mark(Business.TASK, 1)
    t2_tot      = g._total(Business.TASK, 1)

    secAB_mark  = g._mark(Business.SECTION_AB)
    sab_tot     = g._total(Business.SECTION_AB)
    secC_mark   = g._mark(Business.SECTION_C)
    sc_tot      = g._total(Business.SECTION_C)
    prelim_mark = g._mark(Business.PRELIM)
    p_tot       = g._total(Business.PRELIM)

    t1_perc     = g._perc(Business.TASK, 0)
    t2_perc     = g._perc(Business.TASK, 1)
    sab_perc    = g._perc(Business.SECTION_AB)
    sc_perc     = g._perc(Business.SECTION_C)
    p_perc      = g._perc(Business.PRELIM)

    t1_weighted  = g._weighted(Business.TASK, 0)
    t2_weighted  = g._weighted(Business.TASK, 1)
    sab_weighted = g._weighted(Business.SECTION_AB)
    sc_weighted  = g._weighted(Business.SECTION_C)
    p_weighted   = g._weighted(Business.PRELIM)

    total_weighted = t1_weighted + t2_weighted + sab_weighted + sc_weighted + p_weighted

    return {
        "{NAME}":    g.student.name,   "{SURNAME}":     g.student.surname,
        "{SCHOOL}":  getattr(g.student, 'school', ''), "{EXAM_NUMBER}": str(g.student.exam_num),

        "{task1_desc}":     g._desc(Business.TASK, 0, 'Task 1'),
        "{task1_mark}":     t1_mark,  "{task1_total}":    t1_tot,
        "{task1_perc}":     t1_perc,
        "{task1_weighted}": t1_weighted, "{task1_sym}":  g._sym(Business.TASK, 0),

        "{task2_desc}":     g._desc(Business.TASK, 1, 'Task 2'),
        "{task2_mark}":     t2_mark,  "{task2_total}":    t2_tot,
        "{task2_perc}":     t2_perc,
        "{task2_weighted}": t2_weighted, "{task2_sym}":  g._sym(Business.TASK, 1),

        "{secAB_desc}":     g._desc(Business.SECTION_AB, default='Section A and B Test'),
        "{secAB_mark}":     secAB_mark, "{secAB_total}":  sab_tot,
        "{secAB_perc}":     sab_perc,
        "{secAB_weighted}": sab_weighted, "{secAB_sym}": g._sym(Business.SECTION_AB),

        "{secC_desc}":      g._desc(Business.SECTION_C, default='Section C Test'),
        "{secC_mark}":      secC_mark,  "{secC_total}":   sc_tot,
        "{secC_perc}":      sc_perc,
        "{secC_weighted}":  sc_weighted, "{secC_sym}":   g._sym(Business.SECTION_C),

        "{prelim_desc}":        g._desc(Business.PRELIM, default='Preliminary Examination'),
        "{prelim_mark}":        prelim_mark, "{prelim_total}": p_tot,
        "{prelim_perc}":        p_perc,
        "{prelim_weighted}":    p_weighted, "{prelim_sym}": g._sym(Business.PRELIM),

        "{total_weighted}": total_weighted, "{total_sym}": assign_symbol(total_weighted),
    }