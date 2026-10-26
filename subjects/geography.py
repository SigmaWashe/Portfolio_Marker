from core.calculator import round_decimal
from core.constants import Geography
from core.utils import n


def build_data(g):

    research_weighted = n(g._weighted(Geography.RESEARCH))
    tests_weighted = n(g._weighted(Geography.TEST, 0)) + n(g._weighted(Geography.TEST, 1))
    tasks_weighted = n(g._weighted(Geography.TASK, 0)) + n(g._weighted(Geography.TASK, 1)) + n(g._weighted(Geography.TASK, 2))
    prelim_weighted = n(g._weighted(Geography.PRELIM_PAPER_1)) + n(g._weighted(Geography.PRELIM_PAPER_2))
    total = tests_weighted + tasks_weighted + prelim_weighted + research_weighted

    exam_num = f"{g.student.exam_num} "

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam_num[0], "{2}": exam_num[1], "{3}": exam_num[2], "{4}": exam_num[3],
        "{5}": exam_num[4], "{6}": exam_num[5], "{7}": exam_num[6], "{8}": exam_num[7],
        "{9}": exam_num[8], "{10}": exam_num[9], "{11}": exam_num[10], "{12}": exam_num[11], "{13}": exam_num[12],

        "{test1_date}": g._date(Geography.TEST), "{test1_mark}": g._mark(Geography.TEST, 0),
        "{test1_weight}": g._weighted(Geography.TEST, 0), "{test1_total}": g._total(Geography.TEST, 0),

        "{test2_date}": g._date(Geography.TEST), "{test2_mark}": g._mark(Geography.TEST, 1),
        "{test2_weight}": g._weighted(Geography.TEST, 1), "{test2_total}": g._total(Geography.TEST, 2),
        "{sec2_weight}": tests_weighted,

        "{task1_date}": g._date(Geography.TASK), "{task1_mark}": g._mark(Geography.TASK, 0),
        "{task1_weight}": g._weighted(Geography.TASK, 0),

        "{task2_date}": g._date(Geography.TASK), "{task2_mark}": g._mark(Geography.TASK, 1),
        "{task2_weight}": g._weighted(Geography.TASK, 1),

        "{task3_date}": g._date(Geography.TASK), "{task3_mark}": g._mark(Geography.TASK, 2),
        "{task3_weight}": g._weighted(Geography.TASK, 2),
        "{sec1_weight}": tasks_weighted,

        "{prelim1_date}": g._date(Geography.PRELIM_PAPER_1), "{prelim1_mark}": g._mark(Geography.PRELIM_PAPER_1),
        "{prelim2_date}": g._date(Geography.PRELIM_PAPER_2), "{prelim2_mark}": g._mark(Geography.PRELIM_PAPER_2),
        "{prelim_weight}": prelim_weighted, "{prelim_mark}": n(g._mark(Geography.PRELIM_PAPER_1)) + n(g._mark(Geography.PRELIM_PAPER_2)),

        "{proj_date}": g._date(Geography.RESEARCH), "{proj_mark}": g._mark(Geography.RESEARCH),
        "{proj_weight}": research_weighted,
        "{total}": total,
    }