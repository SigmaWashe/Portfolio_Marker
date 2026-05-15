from dataclasses import dataclass
from core.calculator import round_decimal, calculate_percentage, assign_symbol

@dataclass
class Business:
    task1_desc: str
    task1_mark: float
    task1_total: int

    task2_desc: str
    task2_mark: float
    task2_total: int

    sectionA_B_Desc: str
    sectionA_B_Mark: float
    sectionA_B_Total: int

    sectionC_Desc: str
    sectionC_Mark: float
    sectionC_Total: int

    prelim_Desc: str
    prelim_Mark: float
    prelim_total: int = 300

    def markbreakdown(self):
        task1 = calculate_percentage(self.task1_mark, self.task1_total)
        task2 = calculate_percentage(self.task2_mark, self.task2_total)
        sectionA_B = calculate_percentage(self.sectionA_B_Mark, self.sectionA_B_Total)
        section_c = calculate_percentage(self.sectionC_Mark, self.sectionC_Total)
        prelim = calculate_percentage(self.prelim_Mark, self.prelim_total)
        total_sba_mark = (task1 + task2) * 0.2 + sectionA_B * 0.15 + section_c * 0.15 + prelim * 0.3

        return {
            "task1": {
                "description": self.task1_desc, "mark": round_decimal(self.task1_mark, 1),
                "total": self.task1_total, "percentage": round_decimal(task1, 1),
                "sba_mark": round_decimal(task1 * 0.2, 1), "symbol": assign_symbol(task1)
            },
            "task2": {
                "description": self.task2_desc, "mark": round_decimal(self.task2_mark, 1),
                "total": self.task2_total, "percentage": round_decimal(task2, 1),
                "sba_mark": round_decimal(task2 * 0.2, 1), "symbol": assign_symbol(task2)
            },
            "sectionA_B": {
                "description": self.sectionA_B_Desc, "mark": round_decimal(self.sectionA_B_Mark, 1),
                "total": self.sectionA_B_Total, "percentage": round_decimal(sectionA_B, 1),
                "sba_mark": round_decimal(sectionA_B * 0.15, 1), "symbol": assign_symbol(sectionA_B)
            },
            "section_c": {
                "description": self.sectionC_Desc, "mark": round_decimal(self.sectionC_Mark, 1),
                "total": self.sectionC_Total, "percentage": round_decimal(section_c, 1),
                "sba_mark": round_decimal(section_c * 0.15, 1), "symbol": assign_symbol(section_c)
            },
            "prelim": {
                "description": self.prelim_Desc, "mark": round_decimal(self.prelim_Mark, 1),
                "total": self.prelim_total, "percentage": round_decimal(prelim, 1),
                "sba_mark": round_decimal(prelim * 0.3, 1), "symbol": assign_symbol(prelim)
            },
            "total": round_decimal(total_sba_mark, 1),
            "total_symbol": assign_symbol(total_sba_mark)
        }