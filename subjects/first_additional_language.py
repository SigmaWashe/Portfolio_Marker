from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage, assign_symbol
from core.constants import FALTest, FALWeight

@dataclass  
class FirstAdditionalLanguage:
    ext_writing1: float
    ext_writing_total1: int
    ext_writing2: float
    ext_writing_total2: int
    
    cat: float
    cat_total: int
    literature: float
    literature_total: int
    
    test1_mark: float
    test1_total: int
    test2_mark: float
    test2_total: int
    
    test3_mark: float
    test3_total: int
    prelim_mark: float
    prelim_total: int
    
    def markbreakdown(self) -> dict:
        ext1_sym = assign_symbol(calculate_percentage(self.ext_writing1, self.ext_writing_total1))
        ext2_sym = assign_symbol(calculate_percentage(self.ext_writing2, self.ext_writing_total2))
        ext_combined_total = self.ext_writing_total1 + self.ext_writing_total2
        sec1 = round_decimal(calculate_percentage(self.ext_writing1 + self.ext_writing2, ext_combined_total) * 0.30, 1)
        sec1_sym = assign_symbol(calculate_percentage(sec1, 30))

        cat_sym = assign_symbol(calculate_percentage(self.cat, self.cat_total))
        sec2 = round_decimal(calculate_percentage(self.cat, self.cat_total) * 0.20, 1)
        sec2_sym = assign_symbol(calculate_percentage(sec2, 20))

        literature_sym = assign_symbol(calculate_percentage(self.literature, self.literature_total))
        sec3 = round_decimal(calculate_percentage(self.literature, self.literature_total) * 0.20, 1)
        sec3_sym = assign_symbol(calculate_percentage(sec3, 20))

        test1_sym = assign_symbol(calculate_percentage(self.test1_mark, self.test1_total))
        test2_sym = assign_symbol(calculate_percentage(self.test2_mark, self.test2_total))
        test3_sym = assign_symbol(calculate_percentage(self.test3_mark, self.test3_total))
        test_combined_total = self.test1_total + self.test2_total + self.test3_total
        test_combined_mark = self.test1_mark + self.test2_mark + self.test3_mark
        sec4 = round_decimal(calculate_percentage(test_combined_mark, test_combined_total) * 0.10, 1)
        sec4_sym = assign_symbol(calculate_percentage(sec4, 10))

        prep_sym = assign_symbol(calculate_percentage(self.prelim_mark, self.prelim_total))
        sec5 = round_decimal(calculate_percentage(self.prelim_mark, self.prelim_total) * 0.20, 1)
        sec5_sym = assign_symbol(calculate_percentage(sec5, 20))

        total = round_decimal(sec1 + sec2 + sec3 + sec4 + sec5, 1)
        total_sym = assign_symbol(total)

        return {
            "Extended Writing": {
                1: {"total": self.ext_writing_total1, "mark": self.ext_writing1, "symbol": ext1_sym},
                2: {"total": self.ext_writing_total2, "mark": self.ext_writing2, "symbol": ext2_sym, }
            },
            "sec1": sec1, "sec1_symbol": sec1_sym,
            "cat_total": self.cat_total, "cat": self.cat, "cat_symbol": cat_sym,
            "sec2": sec2, "sec2_symbol": sec2_sym,
            "literature_total": self.literature_total, "literature": self.literature,
            "literature_symbol": literature_sym,
            "sec3": sec3, "sec3_symbol": sec3_sym,
            "Test": {
                1: {"total": self.test1_total, "mark": self.test1_mark, "symbol": test1_sym},
                2: {"total": self.test2_total, "mark": self.test2_mark, "symbol": test2_sym},
                3: {"total": self.test3_total, "mark": self.test3_mark, "symbol": test3_sym}
            },
            "sec4": sec4, "sec4_symbol": sec4_sym,
            "prelim_total": self.prelim_total, "prelim_mark": self.prelim_mark, "prelim_symbol": prep_sym,
            "sec5": sec5, "sec5_symbol": sec5_sym,
            "total": total, "total_symbol": total_sym,
        }

    def insert(self, exam_number: int, test_id: int, desc:str, mark:float, total:int):
        conn = get_connection()
        percentage = calculate_percentage(mark, total)
        symbol = assign_symbol(percentage)

        match test_id:
            case FALTest.EXT_WRITING: weighted = round_decimal(percentage * FALTest.EXT_WRITING, 2)
            case FALTest.CAT: weighted = round_decimal(percentage * FALTest.CAT, 2)
            case FALTest.LITERATURE: weighted = round_decimal(percentage * FALTest.LITERATURE, 2)
            case FALTest.PRELIM_PAPER_1: weighted = round_decimal(percentage * FALTest.PRELIM_PAPER_1, 2)
            case FALTest.PRELIM_PAPER_2: weighted = round_decimal(percentage * FALTest.PRELIM_PAPER_2, 2)
            case _: weighted = round_decimal(percentage, 2)

        try:
            conn.execute("""INSERT INTO FirstAdditionalLanguage
                         (exam_number, test_ID, test_description, possible_mark, actual_mark, symbol, weighted_mark)
                         VALUES (?, ?, ?, ?, ?, ?, ?)
                         """, (exam_number, test_id, desc, total, round_decimal(mark, 2), symbol, round_decimal(weighted, 2),))
            conn.commit()
        finally:
            conn.close()

    def delete(self, exam_number: int, id: int):
        conn = get_connection()
        try:
            conn.execute("DELETE FROM FirstAdditionalLanguage WHERE exam_number = ? AND id = ?", (exam_number, id,))
            conn.commit()
        finally:
            conn.close()