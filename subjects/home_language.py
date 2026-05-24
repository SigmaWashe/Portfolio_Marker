from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage, assign_symbol
from core.constants import EngHLTest, EngHLWeight, OtherHLTest, OtherHLWeight

@dataclass
class _HomeLanguage:
    _ext_writing1: float
    _ext_writing2: float
    _test1: float
    _test2: float
    _test3: float
    _prelim_paper1: float
    _prelim_paper2: float
    _prelim_paper1_total: int = 100
    _prelim_paper2_total: int = 100

@dataclass(kw_only=True)
class English(_HomeLanguage):
    cat: float
    literature: float
    lit_total: int

    def markbreakdown(self) -> dict:
        ext1_sym = assign_symbol(calculate_percentage(self._ext_writing1, 45))
        ext2_sym = assign_symbol(calculate_percentage(self._ext_writing2, 45))
        sec1 = round_decimal(self._ext_writing1 + self._ext_writing2, 1)
        sec1_sym = assign_symbol(calculate_percentage(sec1, 90))

        cat_sym = assign_symbol(calculate_percentage(self.cat, 50))
        sec2 = self.cat
        sec2_sym = cat_sym

        lit_sym = assign_symbol(calculate_percentage(self.literature, self.lit_total))
        sec3 = round_decimal(calculate_percentage(self.literature, self.lit_total) * 0.6, 0)
        sec3_sym = assign_symbol(calculate_percentage(sec3, 60))

        test1_sym = assign_symbol(calculate_percentage(self._test1, 20))
        test2_sym = assign_symbol(calculate_percentage(self._test2, 20))
        test3_sym = assign_symbol(calculate_percentage(self._test3, 20))
        sec4 = round_decimal(self._test1 + self._test2 + self._test3, 1)
        sec4_sym = assign_symbol(calculate_percentage(sec4, 60))

        prelim = self._prelim_paper1 + self._prelim_paper2
        prelim_total = self._prelim_paper1_total + self._prelim_paper2_total
        sec5 = round_decimal(calculate_percentage(prelim, prelim_total) * 0.4, 1)
        sec5_sym = assign_symbol(calculate_percentage(sec5, 40))

        total = round_decimal((sec1 + sec2 + sec3 + sec4 + sec5) / 3, 1)
        total_sym = assign_symbol(calculate_percentage(total, 100))

        return {
            "ext1": {"mark": round_decimal(self._ext_writing1, 2), "symbol": ext1_sym},
            "ext2": {"mark": round_decimal(self._ext_writing2, 2), "symbol": ext2_sym},
            "sec1": {"mark": sec1, "symbol": sec1_sym},
            "cat": {"mark": self.cat, "symbol": cat_sym},
            "sec2": {"mark": sec2, "symbol": sec2_sym},
            "literature": {"mark": self.literature, "total": self.lit_total, "symbol": lit_sym},
            "sec3": {"mark": sec3, "symbol": sec3_sym},
            "test1": {"mark": self._test1, "symbol": test1_sym},
            "test2": {"mark": self._test2, "symbol": test2_sym},
            "test3": {"mark": self._test3, "symbol": test3_sym},
            "sec4": {"mark": sec4, "symbol": sec4_sym},
            "prelim": {"mark": prelim, "total": prelim_total, "symbol": assign_symbol(calculate_percentage(prelim, prelim_total))},
            "sec5": {"mark": sec5, "sec5_symbol": sec5_sym},
            "total": {"mark": total, "total_symbol": total_sym},
        }

@dataclass(kw_only=True)
class OtherHl(_HomeLanguage):
    ext_writing1_total: int
    ext_writing2_total: int
    ext_writing3: float
    ext_writing3_total: int
    cat_task1: float
    cat_task2: float
    cat_task2_total: int
    literature: float
    test2_total: int
    test3_total: int
    test4: float
    test4_total: int

    def markbreakdown(self) -> dict:

        # Section 1 - Extended Writing (scaled to 30%)
        ext1_sym = assign_symbol(calculate_percentage(self._ext_writing1, self.ext_writing1_total))
        ext2_sym = assign_symbol(calculate_percentage(self._ext_writing2, self.ext_writing2_total))
        ext3_sym = assign_symbol(calculate_percentage(self.ext_writing3, self.ext_writing3_total))
        ext_total = self.ext_writing1_total + self.ext_writing2_total + self.ext_writing3_total
        sec1 = round_decimal(calculate_percentage(self._ext_writing1 + self._ext_writing2 + self.ext_writing3, ext_total) * 0.3, 1)
        sec1_sym = assign_symbol(calculate_percentage(sec1, 30))

        cat1_sym = assign_symbol(calculate_percentage(self.cat_task1, 20))
        cat2_sym = assign_symbol(calculate_percentage(self.cat_task2, self.cat_task2_total))
        cat_combined_total = 20 + self.cat_task2_total
        sec2 = round_decimal(calculate_percentage(self.cat_task1 + self.cat_task2, cat_combined_total) * 0.2, 1)
        sec2_sym = assign_symbol(calculate_percentage(sec2, 20))

        lit = round_decimal(self.literature, 1)
        lit_sym = assign_symbol(calculate_percentage(lit, 60))
        sec3 = round_decimal(calculate_percentage(lit, 60) * 0.2, 0)
        sec3_sym = assign_symbol(calculate_percentage(sec3, 20))

        test1_sym = assign_symbol(calculate_percentage(self._test1, 20))
        test2_sym = assign_symbol(calculate_percentage(self._test2, self.test2_total))
        test3_sym = assign_symbol(calculate_percentage(self._test3, self.test3_total))
        test4_sym = assign_symbol(calculate_percentage(self.test4, self.test4_total))
        sec4 = round_decimal(calculate_percentage(self._test1 + self._test2 + self._test3 + self.test4,
                                                  20 + self.test2_total + self.test3_total + self.test4_total) * 0.1, 1)
        sec4_sym = assign_symbol(calculate_percentage(sec4, 10))

        prelim = self._prelim_paper1 + self._prelim_paper2
        prelim_total = self._prelim_paper1_total + self._prelim_paper2_total
        sec5 = round_decimal(calculate_percentage(prelim, prelim_total) * 0.2, 1)
        sec5_sym = assign_symbol(calculate_percentage(sec5, 20))

        total = round_decimal((sec1 + sec2 + sec3 + sec4 + sec5) / 3, 1)
        total_sym = assign_symbol(calculate_percentage(total, 100))

        return {
            "ext1": {"mark": self._ext_writing1, "total": self.ext_writing1_total, "symbol": ext1_sym},
            "ext2": {"mark": self._ext_writing2, "total": self.ext_writing2_total, "symbol": ext2_sym},
            "ext3": {"mark": self.ext_writing3, "total": self.ext_writing3_total, "symbol": ext3_sym},
            "sec1": {"mark": sec1, "symbol": sec1_sym},
            "cat1": {"mark": self.cat_task1, "symbol": cat1_sym},
            "cat2": {"mark": self.cat_task2, "total": self.cat_task2_total, "symbol": cat2_sym},
            "sec2": {"mark": sec2, "symbol": sec2_sym},
            "literature": {"mark": lit, "symbol": lit_sym},
            "sec3": {"mark": sec3, "symbol": sec3_sym},
            "test1": {"mark": self._test1, "symbol": test1_sym},
            "test2": {"mark": self._test2, "total": self.test2_total, "symbol": test2_sym},
            "test3": {"mark": self._test3, "total": self.test3_total, "symbol": test3_sym},
            "test4": {"mark": self.test4, "total": self.test4_total, "symbol": test4_sym},
            "sec4": {"mark": sec4, "symbol": sec4_sym},
            "prep": {"mark": prelim, "total": prelim_total, "symbol": assign_symbol(calculate_percentage(prelim, prelim_total))},
            "sec5": {"mark": sec5, "symbol": sec5_sym},
            "total": {"mark": total, "symbol": total_sym},
        }