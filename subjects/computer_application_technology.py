from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage, assign_symbol
from core.constants import CATWeight, CATTest

@dataclass
class ComputerApplicationTechnology:
    theory_date: str
    theory_desc: str
    theory_mark: float
    theory_total: int

    prac_date: str
    prac_desc: str
    prac_mark: float
    prac_total: int

    alt_test_date: str
    alt_test_desc: str
    alt_test_mark: float
    alt_test_total: int

    prelim1_date: str
    prelim1_desc: str
    prelim1_mark: float
    prelim1_total = 180

    prelim2_date: str
    prelim2_desc: str
    prelim2_mark: float
    prelim2_total = 150

    pat_date: str
    pat_desc: str
    pat_mark: float
    pat_total = 170

    def markbreakdown(self):

        theory = calculate_percentage(self.theory_mark, self.theory_total)*0.175
        prac = calculate_percentage(self.prac_mark, self.prac_total)*0.175
        alt_test = calculate_percentage(self.alt_test_mark, self.alt_test_total)*0.15
        prelim1 = calculate_percentage(self.prelim1_mark, self.prelim1_total) * 0.25
        prelim2 = calculate_percentage(self.prelim2_mark, self.prelim2_total) * 0.25
        pat = calculate_percentage(self.pat_mark, self.pat_total)

        return{
            "tests":{
                "theory":{"date": self.theory_date, "description": self.theory_desc, "mark": round_decimal(self.theory_mark, 1),
                          "total": self.theory_total, "actual_mark": round_decimal(theory, 1)},
                "prac":{"date": self.prac_date, "description": self.prac_desc, "mark": round_decimal(self.prac_mark, 1),
                        "total": self.prac_total, "actual_mark": round_decimal(prac, 1)},
                "alt_test":{"date": self.alt_test_date, "description": self.alt_test_desc, "mark": round_decimal(self.alt_test_mark, 1),
                           "total": self.alt_test_total, "actual_mark": round_decimal(alt_test, 1)}
            },
            "prelim":{
                "paper1":{"date": self.prelim1_date, "description": self.prelim1_desc, "mark": round_decimal(self.prelim1_mark, 1),
                          "total": self.prelim1_total, "actual_mark": round_decimal(prelim1, 1)},
                "paper2":{"date": self.prelim2_date, "description": self.prelim2_desc, "mark": round_decimal(self.prelim2_mark, 1),
                          "total": self.prelim2_total, "actual_mark": round_decimal(prelim2, 1)}
            },
            "sba_total": round_decimal(theory + prac + alt_test + prelim1 + prelim2, 1),
            "pat":{"date": self.pat_date, "description": self.pat_desc, "mark": round_decimal(self.pat_mark, 1),
                   "total": self.pat_total, "actual_mark": round_decimal(pat, 1)},
            "total_sba": round_decimal(theory + prac + alt_test + prelim1 + prelim2 + pat, 1)
        }

    def insert(self, exam_number: int , test_id: int, date: str, desc:str, mark:float, total:int):
        conn = get_connection()
        percentage = calculate_percentage(mark, total)

        match test_id:
            case CATTest.THEORY:
                weighted = round_decimal(percentage * CATWeight.THEORY, 2)
                weighted_total = total * CATWeight.THEORY
            case CATTest.PRAC:
                weighted = round_decimal(percentage * CATWeight.PRAC, 2)
                weighted_total = total * CATWeight.PRAC
            case CATTest.ALT_TEST:
                weighted = round_decimal(percentage * CATWeight.PRAC, 2)
                weighted_total = total * CATWeight.PRAC
            case CATTest.PRELIM_1:
                weighted = round_decimal(percentage * CATWeight.PRELIM1, 2)
                weighted_total = total * CATWeight.PRELIM1
            case CATTest.PRELIM_2:
                weighted = round_decimal(percentage * CATWeight.PRELIM2, 2)
                weighted_total = total * CATWeight.PRELIM2
            case CATTest.PAT:
                weighted = round_decimal(percentage, 2)
                weighted_total = total
            case _:
                weighted = round_decimal(percentage, 2)
                weighted_total = total

        try:
            conn.execute("""INSERT INTO ComputerApplicationTechnology
                         (exam_number, test_ID, submission_date, test_description, actual_mark, possible_mark, weighted_mark, weighted_total)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                         """, (exam_number, test_id, date, desc, round_decimal(mark, 2), total, round_decimal(weighted, 2), weighted_total,))
            conn.commit()
        finally:
            conn.close()

    def delete(self, exam_number: int , id: int):
        conn = get_connection()
        try:
            conn.execute("DELETE FROM ComputerApplicationTechnology WHERE exam_number = ? AND id = ?", (exam_number, id,))
            conn.commit()
        finally:
            conn.close()