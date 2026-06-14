from core.calculator import round_decimal, calculate_percentage
from core.constants import LifeSciences
from core.utils import get_center_number

# All four optional test types, in the order they appear in the template
OPTIONAL_TYPES = [
    LifeSciences.RESEARCH_PROJECT,
    LifeSciences.CONTROLLED_WRITING_PIECE,
    LifeSciences.CASE_STUDY,
    LifeSciences.SUMMATIVE_PRACTICAL,
]

OPTIONAL_KEYS = [
    ("{research_topic}", "{research_date}", "{research_mark}", "{research_total}", "{research_weight}"),
    ("{wp_topic}", "{wp_date}", "{wp_mark}", "{wp_total}", "{wp_weight}"),
    ("{case_study_topic}", "{case_study_date}", "{case_study_mark}", "{case_study_total}", "{case_study_weight}"),
    ("{summ_prac_topic}", "{summ_prac_date}", "{summ_prac_mark}", "{summ_prac_total}", "{summ_prac_weight}"),
]

BLANK = ("", "", "", "", "")


def build_data(g):
    prelim1_mark  = g._mark(LifeSciences.PRELIM_PAPER_1)
    prelim2_mark  = g._mark(LifeSciences.PRELIM_PAPER_2)
    prelims_mark  = prelim1_mark + prelim2_mark
    prelims_weight = calculate_percentage(prelims_mark, 300) * 0.25

    # Pick the two optional types with the highest weighted mark
    weighted_scores = [(test_type, g._weighted(test_type)) for test_type in OPTIONAL_TYPES]
    weighted_scores.sort(key=lambda x: x[1], reverse=True)
    chosen = {t for t, _ in weighted_scores[:2]}

    exam_num = g.student.exam_num

    data = {
        "{CENTER_NUM}": get_center_number(exam_num), "{EXAM_NUM}": exam_num,

        "{prelim1_date}": g._date(LifeSciences.PRELIM_PAPER_1), "{prelim1_mark}": g._mark(LifeSciences.PRELIM_PAPER_1),
        "{prelim1_total}": g._total(LifeSciences.PRELIM_PAPER_1),

        "{prelim2_date}": g._date(LifeSciences.PRELIM_PAPER_2), "{prelim2_mark}": g._mark(LifeSciences.PRELIM_PAPER_2),
        "{prelim2_total}": g._total(LifeSciences.PRELIM_PAPER_2),

        "{prelims_mark}":  round_decimal(prelims_mark, 2), "{prelims_weight}": round_decimal(prelims_weight, 2),

        "{test1_topic}": g._desc(LifeSciences.TEST, 0), "{test1_date}": g._date(LifeSciences.TEST),
        "{test1_mark}": g._mark(LifeSciences.TEST, 0), "{test1_total}": g._total(LifeSciences.TEST, 0),
        "{test1_weight}": g._weighted(LifeSciences.TEST, 0),

        "{test2_topic}": g._desc(LifeSciences.TEST, 1), "{test2_date}": g._date(LifeSciences.TEST),
        "{test2_mark}": g._mark(LifeSciences.TEST, 1), "{test2_total}": g._total(LifeSciences.TEST, 1),
        "{test2_weight}": g._weighted(LifeSciences.TEST, 1),

        "{prac_topic}": g._desc(LifeSciences.PRAC), "{prac_date}": g._date(LifeSciences.PRAC),
        "{prac_mark}": g._mark(LifeSciences.PRAC), "{prac_total}": g._total(LifeSciences.PRAC),
        "{prac_weight}": g._weighted(LifeSciences.PRAC),
    }

    for test_type, keys in zip(OPTIONAL_TYPES, OPTIONAL_KEYS):
        topic_k, date_k, mark_k, total_k, weight_k = keys
        if test_type in chosen:
            data[topic_k] = g._desc(test_type)
            data[date_k] = g._date(test_type)
            data[mark_k] = round_decimal(g._mark(test_type), 2)
            data[total_k] = g._total(test_type)
            data[weight_k] = round_decimal(g._weighted(test_type), 2)
        else:
            data[topic_k] = ""
            data[date_k] = ""
            data[mark_k] = ""
            data[total_k] = ""
            data[weight_k] = ""

    chosen_weighted = sum(w for t, w in weighted_scores[:2])
    data["{total}"] = g._weighted(LifeSciences.TEST, 0) + g._weighted(LifeSciences.TEST, 1) + g._weighted(LifeSciences.PRAC) + prelims_weight + chosen_weighted

    return data