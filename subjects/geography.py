from core.calculator import round_decimal
from core.constants import Geography


def build_data(g):

    research_weighted = g._weighted(Geography.RESEARCH)
    tests_weighted = g._weighted(Geography.TEST, 0) + g._weighted(Geography.TEST, 1)
    tasks_weighted = g._weighted(Geography.TASK, 0) + g._weighted(Geography.TASK, 1) + g._weighted(Geography.TASK, 2)
    prelim_weighted = g._weighted(Geography.PRELIM_PAPER_1) + g._weighted(Geography.PRELIM_PAPER_2)
    total = tests_weighted + tasks_weighted + prelim_weighted + research_weighted

    exam = str(g.student.exam_num).zfill(13)

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname,
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "{test1_date}": g._date(Geography.TEST), "{test1_mark}": g._mark(Geography.TEST, 0),
        "{test1_weighted}": g._weighted(Geography.TEST, 0),

        "{test2_date}": g._date(Geography.TEST), "{test2_mark}": g._mark(Geography.TEST, 1),
        "{test2_weighted}": g._weighted(Geography.TEST, 1),
        "{tests_weighted}": tests_weighted,

        "{task1_date}": g._date(Geography.TASK), "{task1_mark}": g._mark(Geography.TASK, 0),
        "{task1_weighted}": g._weighted(Geography.TASK, 0),

        "{task2_date}": g._date(Geography.TASK), "{task2_mark}": g._mark(Geography.TASK, 1),
        "{task2_weighted}": g._weighted(Geography.TASK, 1),

        "{task3_date}": g._date(Geography.TASK), "{task3_mark}": g._mark(Geography.TASK, 2),
        "{task3_weighted}": g._weighted(Geography.TASK, 2),
        "{tasks_total_weighted}": tasks_weighted,

        "{prelim1_date}": g._date(Geography.PRELIM_PAPER_1), "{prelim1_mark}": g._mark(Geography.PRELIM_PAPER_1),
        "{prelim2_date}": g._date(Geography.PRELIM_PAPER_2), "{prelim2_mark}": g._mark(Geography.PRELIM_PAPER_2),
        "{prelim_weighted}": prelim_weighted,

        "{proj_date}": g._date(Geography.RESEARCH), "{proj_mark}": g._mark(Geography.RESEARCH),
        "{proj_weighted}": research_weighted,
        "{total}": total,
    }