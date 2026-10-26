from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage
from core.constants import History
from core.utils import n

def build_data(g):
    test1 = n(g._mark(History.TEST, 0))
    test2 = n(g._mark(History.TEST, 1))
    test3 = n(g._mark(History.TEST, 2))
    prelim = n(g._mark(History.PRELIM_PAPER_1)) + n(g._mark(History.PRELIM_PAPER_2))
    total = test1 + test2 + test3 + prelim

    history_inv = g._mark(History.HIST_INV)
    source_analysis = g._mark(History.SOURCE_ANALYSIS)
    source_based_essay = g._mark(History.SOURCE_BASED_ESSAY)
    visual_analysis = g._mark(History.VISUAL_ANALYSIS)
    secB_alt = n(source_analysis) + n(source_based_essay) + n(visual_analysis)

    exam_num = f"{g.student.exam_num} "

    results = {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam_num[0], "{2}": exam_num[1], "{3}": exam_num[2], "{4}": exam_num[3],
        "{5}": exam_num[4], "{6}": exam_num[5], "{7}": exam_num[6], "{8}": exam_num[7],
        "{9}": exam_num[8], "{10}": exam_num[9], "{11}": exam_num[10], "{12}": exam_num[11], "{13}": exam_num[12],

        "{test1_mark}": g._mark(History.TEST, 0), "{test1_total}": g._total(History.TEST, 0), "{test1_weighted}": g._weighted(History.TEST, 0),
        "{test2_mark}": g._mark(History.TEST, 1), "{test2_total}": g._total(History.TEST, 1), "{test2_weighted}": g._weighted(History.TEST, 1),
        "{test3_mark}": g._mark(History.TEST, 2), "{test3_total}": g._total(History.TEST, 2), "{test3_weighted}": g._weighted(History.TEST, 2),
        "{secA_weighted}": n(g._weighted(History.TEST, 0)) + n(g._weighted(History.TEST, 1)) + n(g._weighted(History.TEST, 2)),

        "{prelim1_mark}": g._mark(History.PRELIM_PAPER_1, 0), "{prelim2_mark}": g._mark(History.PRELIM_PAPER_2, 1),
        "{prelims_weighted}": n(g._mark(History.PRELIM_PAPER_1, 0)) + n(g._mark(History.PRELIM_PAPER_2, 1)),
    }

    if n(history_inv) > secB_alt:
        total += n(g._weighted(History.HIST_INV))
        results.update({"{history_inv_mark}": history_inv, "{history_inv_weighted}": g._weighted(History.HIST_INV),
                        "{secB_weighted}": g._weighted(History.HIST_INV)})
        results.update({"{source_analysis_mark}": '', "{source_essay_mark}": '', "{vis_analysis_mark}": ''})
    else:
        total += secB_alt
        results.update({"{source_analysis_mark}": source_analysis, "{source_essay_mark}": source_based_essay, "{vis_analysis_mark}": visual_analysis,
        "{secB_weighted}": n(g._weighted(History.SOURCE_ANALYSIS)) + n(g._weighted(History.SOURCE_BASED_ESSAY)) + n(g._weighted(History.VISUAL_ANALYSIS))})
        results.update({"{history_inv_mark}": '', "{history_inv_weighted}": ''})
    results.update({"{total}": total})

    return results