from core.constants import Accounting


def build_data(g):
    prelim1 = g._weighted(Accounting.PRELIM_PAPER_1)
    prelim2 = g._weighted(Accounting.PRELIM_PAPER_2)
    test1 = g._weighted(Accounting.TEST, 0)
    test2 = g._weighted(Accounting.TEST, 1)
    test3 = g._weighted(Accounting.TEST, 2)
    choice_assessment = g._weighted(Accounting.CHOICE_ASSESSMENT_TASK)

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname, "{EXAM_NUM}": str(g.student.exam_num), "{SCHOOL}": g.student.school,

        "{prelim_weighted}": prelim1+prelim2, "{test1_weighted}": test1, "{test2_weighted}": test2, "{test3_weighted}": test3,
        "{alt_weighted}": choice_assessment, "{total}": prelim1 + prelim2 + test1 + test2 + test3 + choice_assessment
    }