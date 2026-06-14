from core.constants import PhysicalSciences as Physics
from core.utils import get_center_number

def build_data(g):
    exam_num = g.studentexam_num
    return {
        "{NAME}": g.student.name, "{SURNAME}": g.student.surname, "{EXAM_NUM}": exam_num, "CENTER_NUM": get_center_number(exam_num),

        "{prac1_date}": g._date(Physics.PHYS_PRAC), "{prac1_total}": g._total(Physics.PHYS_PRAC), "{prac1_mark}": g._mark(Physics.PHYS_PRAC),
        "{prac1_perc}": g._perc(Physics.PHYS_PRAC), "{prac1_weight}": g._weight(Physics.PHYS_PRAC),

        "{prac2_date}": g._date(Physics.CHEM_PRAC), "{prac2_total}": g._total(Physics.CHEM_PRAC), "{prac2_mark}": g._mark(Physics.CHEM_PRAC),
        "{prac2_perc}": g._perc(Physics.CHEM_PRAC), "{prac2_weight}": g._weight(Physics.CHEM_PRAC),

        "{phys_date}": g._date(Physics.PHYS_TEST), "{phys_total}": g._total(Physics.PHYS_TEST), "{phys_mark}": g._mark(Physics.PHYS_TEST),
        "{phys_perc}": g._perc(Physics.PHYS_TEST), "{phys_weight}": g._weight(Physics.PHYS_TEST),

        "{chem_date}": g._date(Physics.CHEM_TEST), "{chem_total}": g._total(Physics.CHEM_TEST), "{chem_mark}": g._mark(Physics.CHEM_TEST),
        "{chem_perc}": g._perc(Physics.CHEM_TEST), "{chem_weight}": g._weight(Physics.CHEM_TEST),

        "{prelim1_date}": g._date(Physics.PRELIM_1), "{prelim1_total}": g._total(Physics.PRELIM_1), "{prelim1_mark}": g._mark(Physics.PRELIM_1),
        "{prelim1_perc}": g._perc(Physics.PRELIM_1), "{prelim1_weight}": g._weight(Physics.PRELIM_1),

        "{prelim2_date}": g._date(Physics.PRELIM_2), "{prelim2_total}": g._total(Physics.PRELIM_2), "{prelim2_mark}": g._mark(Physics.PRELIM_2),
        "{prelim2_perc}": g._perc(Physics.PRELIM_2), "{prelim2_weight}": g._weight(Physics.PRELIM_2),

        "total": g._weight(Physics.PHYS_PRAC) + g._weight(Physics.CHEM_PRAC) + g._weight(Physics.PHYS_TEST) +
                 g._weight(Physics.CHEM_TEST) + g._weight(Physics.PRELIM_1) + g._weight(Physics.PRELIM_2),
    }