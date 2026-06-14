from core.constants import Economics


def build_data(g):
    tests_perc = g._perc(Economics.CONTROLLED_TEST, 0) + g._perc(Economics.CONTROLLED_TEST, 1)
    tests_weight = g._weighted(Economics.CONTROLLED_TEST, 0) + g._weighted(Economics.CONTROLLED_TEST, 1)

    prelim_weight = g._weighted(Economics.PRELIM)
    multi_weight = g._weighted(Economics.MULTIPLE_CHOICE)
    task_weight = g._weighted(Economics.DATA_RESPONSE)
    oral_weight = g._weighted(Economics.ORAL)


    return{
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname, "{SCHOOL}": getattr(g.student, 'school', ''),
        "{EXAM_NUMBER}": g.student.exam_num,

        "{prelim_date}": g._date(Economics.PRELIM), "prelim_perc": g._perc(Economics.PRELIM), "prelim_weight": prelim_weight,
        "{test_date}"  : g._date(Economics.CONTROLLED_TEST), "test_perc" : tests_perc, "test_weight": tests_weight,
        "{multi_date}" : g._date(Economics.MULTIPLE_CHOICE), "multi_perc": g._perc(Economics.MULTIPLE_CHOICE), "multi_weight": multi_weight,
        "{task_date}"  : g._date(Economics.DATA_RESPONSE), "task_perc" : g._perc(Economics.DATA_RESPONSE), "task_weight": task_weight,
        "{oral_date}"  : g._date(Economics.ORAL), "oral_perc": g._perc(Economics.ORAL), "oral_weight": oral_weight,

        "{total}" : tests_weight + prelim_weight + multi_weight + task_weight + oral_weight

    }