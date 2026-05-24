from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage, assign_symbol
from core.constants import GeographyTest, GeographyWeight

@dataclass
class Geography:
    
    _task1_date: str
    _task1_mark: float
    _task2_date: str
    _task2_mark: float
    
    _task3_date: str
    _task3_mark: float
    _task_total = 100
    
    _research_date: str
    _research_mark: float
    _research_total = 100
    
    _test1_date: str
    _test1_mark: float
    _test2_date: str
    _test2_mark: float
    _test_total = 100
    
    _prelim1_date: str
    _prelim1_mark: float
    _prelim1_total = 200
    
    _prelim2_date: str
    _prelim2_mark: float
    _prelim2_total = 100

    def markbreakdown(self):
        test1 = calculate_percentage(self._test1_mark, self._test_total)*0.15
        test2 = calculate_percentage(self._test2_mark, self._test_total)*0.15
        prelim = calculate_percentage(self._prelim1_mark+self._prelim2_mark, 300)*0.25

        task1 = calculate_percentage(self._task1_mark, self._task_total) * 0.15
        task2 = calculate_percentage(self._task2_mark, self._task_total) * 0.15
        task3 = calculate_percentage(self._task3_mark, self._task_total) * 0.15

        total = test1 + test2 + prelim
        task_final = task1 + task2 + task3
        research_task = calculate_percentage(self._research_mark, self._research_total) * 0.30

        if task_final < research_task:
            total += task_final
        else:
            total += research_task

        return {
            "Controlled Tests": {
                1: {"date": self._test1_date, "mark": round_decimal(self._test1_mark, 1), "weighted": round_decimal(test1, 1)},
                2: {"date": self._test2_date, "mark": round_decimal(self._test2_mark, 1), "weighted": round_decimal(test2, 1)},
                "total_weighted": round_decimal(test1 + test2, 1)
            },
            "Prelim": {
                1: {"date": self._prelim1_date, "mark": round_decimal(self._prelim1_mark, 1)},
                2: {"date": self._prelim2_date, "mark": round_decimal(self._prelim2_mark, 1)},
                "Total": round_decimal(self._prelim1_mark + self._prelim2_mark, 1), "Weighted": round_decimal(prelim, 1)
            },
            "Assessment Task": {
                1: {"date": self._task1_date, "mark": round_decimal(self._task1_mark, 1), "weighted": round_decimal(task1, 1)},
                2: {"date": self._task2_date, "mark": round_decimal(self._task2_mark, 1), "weighted": round_decimal(task2, 1)},
                3: {"date": self._task3_date, "mark": round_decimal(self._task3_mark, 1), "weighted": round_decimal(task3, 1)},
                "total_weighted": round_decimal(task1 + task2 + task3, 1)
            },
            "Research Task": {
                "date": self._research_date, "mark": round_decimal(self._research_mark, 1), "weighted": round_decimal(research_task, 1)
            },
            "Total": round_decimal(total, 1)
        }