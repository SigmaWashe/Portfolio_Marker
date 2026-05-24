from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage
from core.constants import LifeSciencesTest, LifeSciencesWeight

@dataclass
class LifeSciences:

    _paper1_date: str
    _paper1_mark: float
    _paper2_date: str
    _paper2_mark: float

    _test1_topic: str
    _test1_date: str
    _test1_mark: float
    _test1_total: int

    _test2_topic: str
    _test2_date: str
    _test2_mark: float
    _test2_total: int

    _prac_topic: str
    _prac_date: str
    _prac_mark: float
    _prac_total: int

    _task1_topic: str
    _task1_date: str
    _task1_mark: float
    _task1_total: int

    _task2_topic: str
    _task2_date: str
    _task2_mark: float
    _task2_total: int

    def markbreakdown(self):

        prelim = calculate_percentage(self._paper1_mark+self._paper2_mark, 300) * 0.25
        test1 = calculate_percentage(self._test1_mark, self._test1_total) * 0.15
        test2 = calculate_percentage(self._test2_mark, self._test2_total) * 0.15
        prac = calculate_percentage(self._prac_mark, self._prac_total) * 0.15
        task1 = calculate_percentage(self._task1_mark, self._task1_total) * 0.15
        task2 = calculate_percentage(self._task2_mark, self._task2_total) * 0.15

        return {
            "Prelims": {
                "Paper1": {"date": self._paper1_date, "mark": round_decimal(self._paper1_mark, 1)},
                "Paper2": {"date": self._paper2_date, "mark": round_decimal(self._paper2_mark, 1)},
                "Total": round_decimal(self._paper1_mark + self._paper2_mark, 1), "Weighted": round_decimal(prelim, 1)
            },
            "Tests":{
                1: {"topic": self._test1_topic, "date": self._test1_date, "mark": self._test1_mark,
                      "total": self._test1_total, "weighted": round_decimal(test1, 1)},
                2: {"topic": self._test2_topic, "date": self._test2_date, "mark": self._test2_mark,
                      "total": self._test2_total, "weighted": round_decimal(test2, 1)},
                "Prac": {"topic": self._prac_topic, "date": self._prac_date, "mark": self._prac_mark,
                      "total": self._prac_total, "weighted": round_decimal(prac, 1)},
            },
            "Tasks": {
                1: {"topic": self._task1_topic, "date": self._task1_date, "mark": self._task1_mark,
                      "total": self._task1_total, "weighted": round_decimal(task1, 1)},
                2: {"topic": self._task2_topic, "date": self._task2_date, "mark": self._task2_mark,
                      "total": self._task2_total, "weighted": round_decimal(task2, 1)}
            },
            "Total": round_decimal(prelim + test1 + test2 + prac + task1 + task2, 1)
        }