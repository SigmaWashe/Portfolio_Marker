from core.constants import DramaticArts

def build_data(g):

    prac1 = g._weighted(DramaticArts.PRACTICAL, 0)
    prac2 = g._weighted(DramaticArts.PRACTICAL, 1)
    prac3 = g._weighted(DramaticArts.PRACTICAL, 2)
    prac  = g._mark(DramaticArts.PRACTICAL, 0) + g._mark(DramaticArts.PRACTICAL, 1) + g._mark(DramaticArts.PRACTICAL, 2)

    theory1 = g._weighted(DramaticArts.THEORY, 0)
    theory2 = g._weighted(DramaticArts.THEORY, 1)
    theory3 = g._weighted(DramaticArts.THEORY, 2)
    prelim = g._weighted(DramaticArts.PRELIM)
    theory = g._mark(DramaticArts.THEORY, 0) + g._mark(DramaticArts.THEORY, 1) + g._mark(DramaticArts.THEORY, 2) + g._mark(DramaticArts.PRELIM)

    pat_A  = g._weighted(DramaticArts.PAT_SECTION_A)
    pat_B  = g._weighted(DramaticArts.PAT_SECTION_B)

    exam = str(g.student.exam_num).zfill(13)

    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname, "{SCHOOL}": getattr(g.student, 'school', ''),
        "{1}": exam[0],  "{2}": exam[1],  "{3}": exam[2],  "{4}": exam[3],
        "{5}": exam[4],  "{6}": exam[5],  "{7}": exam[6],  "{8}": exam[7],
        "{9}": exam[8],  "{10}": exam[9], "{11}": exam[10], "{12}": exam[11], "{13}": exam[12],

        "{prac1_desc}": g._desc(DramaticArts.PRACTICAL, 0), "{prac1_mark}": g._mark(DramaticArts.PRACTICAL, 0),
        "{prac2_desc}": g._desc(DramaticArts.PRACTICAL, 1), "{prac2_mark}": g._mark(DramaticArts.PRACTICAL, 1),
        "{prac3_desc}": g._desc(DramaticArts.PRACTICAL, 2), "{prac3_mark}": g._mark(DramaticArts.PRACTICAL, 2),
        "{prac_mark}" : prac,

        "{theory1_desc}": g._desc(DramaticArts.THEORY, 0), "{theory1_mark}": g._mark(DramaticArts.THEORY, 0),
        "{theory2_desc}": g._desc(DramaticArts.THEORY, 1), "{theory2_mark}": g._mark(DramaticArts.THEORY, 1),
        "{theory3_desc}": g._desc(DramaticArts.THEORY, 2), "{theory3_mark}": g._mark(DramaticArts.THEORY, 2),
        "{prelim}_desc}": g._desc(DramaticArts.PRELIM),    "{prelim}_mark}": g._mark(DramaticArts.PRELIM),
        "{theory_mark}" : theory,

        "{sba_weight}"  : theory + prac,

        "{secA_desc}"   : g._desc(DramaticArts.PAT_SECTION_A), "{secA_mark}": g._mark(DramaticArts.PAT_SECTION_A),
        "{secB_desc}"   : g._desc(DramaticArts.PAT_SECTION_B), "{secB_mark}": g._mark(DramaticArts.PAT_SECTION_B),
        "{pat_mark}"    : g._mark(DramaticArts.PAT_SECTION_A) + g._mark(DramaticArts.PAT_SECTION_B),
        "{pat_weight}"  : pat_A + pat_B,
    }