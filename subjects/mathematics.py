from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage, assign_symbol
from core.constants import MathematicsTest, MathematicsWeight

@dataclass
class Mathematics:
    _short_item1_desc: str
    _short_item1_mark: float
    _short_item1_total: int

    _short_item2_desc: str
    _short_item2_mark: float
    _short_item2_total: int

    _long_item_desc: str
    _long_item_mark: float
    _long_item_total: int

    _test1_desc: str
    _test1_mark: float
    _test1_total: int

    _test2_desc: str
    _test2_mark: float
    _test2_total: int

    _test3_desc: str
    _test3_mark: float
    _test3_total: int

    _prelim1_mark: float
    _prelim1_total: int
    _prelim2_mark: float
    _prelim2_total: int

    def markbreakdown(self):
        short1_perc = calculate_percentage(self._short_item1_mark, self._short_item1_total)
        short2_perc = calculate_percentage(self._short_item2_mark, self._short_item2_total)
        long_perc = calculate_percentage(self._long_item_mark, self._long_item_total)

        test1_perc = calculate_percentage(self._test1_mark, self._test1_total)
        test2_perc = calculate_percentage(self._test2_mark, self._test2_total)
        test3_perc = calculate_percentage(self._test3_mark, self._test3_total)

        prelim1_perc = calculate_percentage(self._prelim1_mark, 150)
        prelim2_perc = calculate_percentage(self._prelim2_mark, 150)

        short_final = round_decimal((short1_perc * 0.15) + (short2_perc * 0.15), 1)
        long_final = round_decimal(long_perc * 0.3, 1)
        test_final = round_decimal((test1_perc * 0.1) + (test2_perc * 0.1) + (test3_perc * 0.1), 1)
        prelim1_final = round_decimal((prelim1_perc * 0.2), 1)
        prelim2_final = round_decimal((prelim2_perc * 0.2), 1)

        final_sba = test_final + prelim1_final + prelim2_final
        if short_final > long_final:
            final_sba += short_final
        else:
            final_sba += long_final

        final_perc = round_decimal(final_sba, 1)
        final_symbol = assign_symbol(final_perc)

        return {
            "short_item": {
                1: {"description": self._short_item1_desc, "mark": round_decimal(self._short_item1_mark, 1),
                    "total": int(self._short_item1_total), "percentage": round_decimal(short1_perc, 1), "symbol": assign_symbol(short1_perc)
                    },
                2: {"description": self._short_item2_desc, "mark": round_decimal(self._short_item2_mark, 1),
                    "total": int(self._short_item2_total), "percentage": round_decimal(short2_perc, 1), "symbol": assign_symbol(short2_perc)
                    },
                "weighted_final": short_final
            },

            "long_item": {"description": self._long_item_desc, "mark": round_decimal(self._long_item_mark, 1),
                          "total": int(self._long_item_total), "percentage": round_decimal(long_perc, 1),
                          "symbol": assign_symbol(long_perc), "weighted_final": long_final
                          },

            "test": {
                1: {"description": self._test1_desc, "mark": round_decimal(self._test1_mark, 1), "total": int(self._test1_total),
                    "percentage": round_decimal(test1_perc, 1), "symbol": assign_symbol(test1_perc)},
                2: {"description": self._test2_desc, "mark": round_decimal(self._test2_mark, 1),
                          "total": int(self._test2_total),
                          "percentage": round_decimal(test2_perc, 1), "symbol": assign_symbol(test2_perc)
                          },
                3: {"description": self._test3_desc, "mark": round_decimal(self._test3_mark, 1),
                          "total": int(self._test3_total),
                          "percentage": round_decimal(test3_perc, 1), "symbol": assign_symbol(test3_perc)
                          },
                "weighted_final": test_final
            },

            "prelim": {
                "paper1": {"mark": round_decimal(self._prelim1_mark, 1), "total": 300,
                           "percentage": round_decimal(prelim1_perc, 1), "symbol": assign_symbol(prelim1_perc),
                           "weighted_final": prelim1_final
                           },
                "paper2": {"mark": round_decimal(self._prelim2_mark, 1), "total": 300,
                           "percentage": round_decimal(prelim2_perc, 1), "symbol": assign_symbol(prelim2_perc),
                           "weighted_final": prelim2_final
                           }
            },

            "final": {
                "percentage": final_perc,
                "symbol": final_symbol
            }
        }