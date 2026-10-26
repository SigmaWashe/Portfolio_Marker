from core.constants import DramaticArts
from core.utils import n

def build_data(g):

    prac1 = n(g._weighted(DramaticArts.PRACTICAL, 0))
    prac2 = n(g._weighted(DramaticArts.PRACTICAL, 1))
    prac3 = n(g._weighted(DramaticArts.PRACTICAL, 2))
    prac  = n(g._mark(DramaticArts.PRACTICAL, 0)) + n(g._mark(DramaticArts.PRACTICAL, 1)) + n(g._mark(DramaticArts.PRACTICAL, 2))

    theory1 = n(g._weighted(DramaticArts.THEORY, 0))
    theory2 = n(g._weighted(DramaticArts.THEORY, 1))
    theory3 = n(g._weighted(DramaticArts.THEORY, 2))
    prelim = n(g._weighted(DramaticArts.PRELIM))
    theory = n(g._mark(DramaticArts.THEORY, 0)) + n(g._mark(DramaticArts.THEORY, 1)) + n(g._mark(DramaticArts.THEORY, 2)) + n(g._mark(DramaticArts.PRELIM))

    pat_A  = n(g._weighted(DramaticArts.PAT_SECTION_A))
    pat_B  = n(g._weighted(DramaticArts.PAT_SECTION_B))

    exam_num = f"{g.student.exam_num} "

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname, "{SCHOOL}": getattr(g.student, 'school', ''),
        "{1}": exam_num[0], "{2}": exam_num[1], "{3}": exam_num[2], "{4}": exam_num[3],
        "{5}": exam_num[4], "{6}": exam_num[5], "{7}": exam_num[6], "{8}": exam_num[7],
        "{9}": exam_num[8], "{10}": exam_num[9], "{11}": exam_num[10], "{12}": exam_num[11], "{13}": exam_num[12],

        "{prac1_desc}": g._desc(DramaticArts.PRACTICAL, 0), "{prac1_mark}": g._mark(DramaticArts.PRACTICAL, 0),
        "{prac2_desc}": g._desc(DramaticArts.PRACTICAL, 1), "{prac2_mark}": g._mark(DramaticArts.PRACTICAL, 1),
        "{prac3_desc}": g._desc(DramaticArts.PRACTICAL, 2), "{prac3_mark}": g._mark(DramaticArts.PRACTICAL, 2),
        "{prac_mark}" : prac,

        "{theory1_desc}": g._desc(DramaticArts.THEORY, 0), "{theory1_mark}": g._mark(DramaticArts.THEORY, 0),
        "{theory2_desc}": g._desc(DramaticArts.THEORY, 1), "{theory2_mark}": g._mark(DramaticArts.THEORY, 1),
        "{theory3_desc}": g._desc(DramaticArts.THEORY, 2), "{theory3_mark}": g._mark(DramaticArts.THEORY, 2),
        "{prelim_desc}" : g._desc(DramaticArts.PRELIM),    "{prelim_mark}" : g._mark(DramaticArts.PRELIM),
        "{theory_mark}" : theory,

        "{sba_mark}" : theory + prac, "{sba_weight}"  : theory1 + prac1 + theory2 + prac2 + theory3 + prac3 + prelim,

        "{secA_desc}"   : g._desc(DramaticArts.PAT_SECTION_A), "{secA_mark}": g._mark(DramaticArts.PAT_SECTION_A),
        "{secB_desc}"   : g._desc(DramaticArts.PAT_SECTION_B), "{secB_mark}": g._mark(DramaticArts.PAT_SECTION_B),
        "{pat_mark}"    : n(g._mark(DramaticArts.PAT_SECTION_A)) + n(g._mark(DramaticArts.PAT_SECTION_B)),
        "{pat_weight}"  : pat_A + pat_B,
    }