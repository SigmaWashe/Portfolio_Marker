from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage
from core.constants import ITTest, ITWeight

@dataclass
class InformationTechnology:

    _pat_desc: str
    _pat_mark: float
    _pat_total: int

    _theory_desc: str
    _theory_mark: float
    _theory_total: int

    _prac_desc: str
    _prac_mark: float
    _prac_total: int

    _alt_desc: str
    _alt_mark: float
    _alt_total: int

    _prelim_prac_desc: str
    _prelim_prac_mark: float

    _prelim_theory_desc: str
    _prelim_theory_mark: float

    def markbreakdown(self):
        pat = calculate_percentage(self._pat_mark, self._pat_total)
        theory = calculate_percentage(self._theory_mark, self._theory_total) * 0.175
        prac = calculate_percentage(self._prac_mark, self._prac_total) * 0.175
        alt = calculate_percentage(self._alt_mark, self._alt_total) * 0.15
        prelim_theory = calculate_percentage(self._prelim_theory_mark, 150) * 0.25
        prelim_prac = calculate_percentage(self._prelim_prac_mark, 150) * 0.25
        return {
            "PAT": {"desc": self._pat_desc, "mark": round_decimal(pat, 2), "final": round_decimal(pat, 0)},
            "Theory": {"desc": self._theory_desc, "mark": round_decimal(theory, 2)},
            "Prac": {"desc": self._prac_desc, "mark": round_decimal(prac, 2)},
            "Alt": {"desc": self._alt_desc, "mark": round_decimal(alt, 2)},
            "Prelim Theory": {"desc": self._prelim_theory_desc, "mark": round_decimal(prelim_theory, 2)},
            "Prelim Prac": {"desc": self._prelim_prac_desc, "mark": round_decimal(prelim_prac, 2)},
            "SBA Final": round_decimal(pat+theory+prac+alt+prelim_theory+prelim_prac, 0)
        }