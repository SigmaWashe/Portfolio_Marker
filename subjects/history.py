from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage
from core.constants import HistoryTest, HistoryWeight

@dataclass
class History:
    _test1: float
    _test1_total: int
    _test2: float
    _test2_total: int
    _test3: float
    _test3_total: int

    _prelim1: float
    _prelim2: float
    _hist_inv: float
    _source_analysis: float
    _source_based_essay: float
    _visual_analysis: float

    def __init__(self, test1:float, test1_total:int, test2:float, test2_total:int, test3:float, test3_total,
                 prelim1:float, prelim2:float, hist_inv:float, source_analysis:float, source_based_essay:float, visual_analysis:float):
        self._test1 = test1
        self._test1_total = test1_total
        self._test2 = test2
        self._test2_total = test2_total
        self._test3 = test3
        self._test3_total = test3_total
        self._prelim1 = prelim1
        self._prelim2 = prelim2
        self._hist_inv = hist_inv
        self._source_analysis = source_analysis
        self._source_based_essay = source_based_essay
        self._visual_analysis = visual_analysis

    def markbreakdown(self):
        test1 = calculate_percentage(self._test1, self._test1_total) * 0.10
        test2 = calculate_percentage(self._test2, self._test2_total) * 0.10
        test3 = calculate_percentage(self._test3, self._test3_total) * 0.10
        prelim = calculate_percentage(self._prelim1+self._prelim2, 300)*0.25
        result = {
            "Tests": {
                1: {"mark": round_decimal(self._test1, 1), "total": self._test1_total, "weighted": round_decimal(test1, 1)},
                2: {"mark": round_decimal(self._test2, 1), "total": self._test2_total, "weighted": round_decimal(test2, 1)},
                3: {"mark": round_decimal(self._test3, 1), "total": self._test3_total, "weighted": round_decimal(test3, 1)},
                "total_weighted": round_decimal(test1 + test2 + test3, 1)},
            "Prelim":{"Paper1": round_decimal(self._prelim1, 1), "Paper2": round_decimal(self._prelim2, 1),
                      "Weighted": round_decimal(prelim, 1)}
        }
        total = test1+test2+test3+prelim
        hist_inv = calculate_percentage(self._hist_inv, 45)
        source_analysis = calculate_percentage(self._source_analysis, 15)
        source_based_essay = calculate_percentage(self._source_based_essay, 15)
        visual_analysis = calculate_percentage(self._visual_analysis, 15)
        secB = source_analysis + source_based_essay + visual_analysis

        if hist_inv > secB:
            total += hist_inv
            result["Historical Investigation"] = {"mark": round_decimal(self._hist_inv, 1), "weighted": round_decimal(hist_inv, 1)*0.45}
        else:
            total += secB
            result["Section B"] = {"Source Analysis": round_decimal(self._source_analysis, 1),
                                   "Source Based Essay": round_decimal(self._source_based_essay, 1),
                                   "Visual Analysis": round_decimal(self._visual_analysis, 1),
                                   "weighted": round_decimal(source_analysis*0.15 + source_based_essay*0.15 + visual_analysis*0.15, 1)
                                   }

        result["Total"] = {"total": round_decimal(total, 1)}

        return result