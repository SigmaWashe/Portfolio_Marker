from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage
from core.constants import History

def build_data(g):
    test1 = g._mark(History.TEST, 0)
    test2 = g._mark(History.TEST, 1)
    test3 = g._mark(History.TEST, 2)
    prelim = g._mark(History.PRELIM_PAPER_1) + g._mark(History.PRELIM_PAPER_2)
    total = test1 + test2 + test3 + prelim

    history_inv = g._mark(History.HIST_INV)
    source_analysis = g._mark(History.SOURCE_ANALYSIS)
    source_based_essay = g._mark(History.SOURCE_BASED_ESSAY)
    visual_analysis = g._mark(History.VISUAL_ANALYSIS)
    secB_alt = source_analysis + source_based_essay + visual_analysis

    exam = str(g.student.exam_num).zfill(13)

    results = {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "test1_mark": g._mark(History.TEST, 0), "test1_total": g._total(History.TEST, 0), "test1_weighted": g._weighted(History.TEST, 0),
        "test2_mark": g._mark(History.TEST, 1), "test2_total": g._total(History.TEST, 1), "test2_weighted": g._weighted(History.TEST, 1),
        "test3_mark": g._mark(History.TEST, 2), "test3_total": g._total(History.TEST, 2), "test3_weighted": g._weighted(History.TEST, 2),
        "{secA_weighted}": g._weighted(History.TEST, 0) + g._weighted(History.TEST, 1) + g._weighted(History.TEST, 2),

        "{prelim1_mark}": g._mark(History.PRELIM_PAPER_1, 0), "{prelim2_mark}": g._mark(History.PRELIM_PAPER_2, 1),
        "{prelims_weighted}": g._mark(History.PRELIM_PAPER_1, 0) + g._mark(History.PRELIM_PAPER_2, 1),
    }

    if history_inv > secB_alt:
        total += g._weighted(History.HIST_INV)
        results += {"{history_inv_mark}": history_inv, "{history_inv_weighted}": g._weighted(History.HIST_INV),
                    "{secB_weighted}": g._weighted(History.HIST_INV)}
        results += {"{source_analysis_mark}": '', "{source_essay_mark}": '', "{vis_analysis_mark}": ''}
    else:
        total += secB_alt
        results += {"{source_analysis_mark}": source_analysis, "{source_essay_mark}": source_based_essay, "{vis_analysis_mark}": visual_analysis,
        "{secB_weighted}": g._weighted(History.SOURCE_ANALYSIS) + g._weighted(History.SOURCE_BASED_ESSAY) + g._weighted(History.VISUAL_ANALYSIS)}
        results += {"{history_inv_mark}": '', "{history_inv_weighted}": ''}
    results += {"total": total}

    return results