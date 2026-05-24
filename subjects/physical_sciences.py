from dataclasses import dataclass

from core.calculator import round_decimal, calculate_percentage

@dataclass
class PhysicalSciences:

    _phys_prac_date: str
    _phys_prac_mark:  float
    _phys_prac_total: int
    _chem_prac_date: str
    _chem_prac_mark:  float
    _chem_prac_total: int

    _phys_test_date: str
    _phys_test_mark:  float
    _phys_test_total: int
    _chem_test_date: str
    _chem_test_mark:  float
    _chem_test_total: int

    _paper1_date: str
    _paper1_mark: int
    _paper2_date: str
    _paper2_mark: int

    def markbreakdown(self):
        phys_prac = calculate_percentage(self._phys_prac_mark, self._phys_prac_total)
        chem_prac = calculate_percentage(self._chem_prac_mark, self._chem_prac_total)
        phys_test = calculate_percentage(self._phys_test_mark, self._phys_test_total)
        chem_test = calculate_percentage(self._chem_test_mark, self._chem_test_total)
        paper1 = calculate_percentage(self._paper1_mark, 200)
        paper2 = calculate_percentage(self._paper2_mark, 200)

        return {
            "Investigations": {
                "Physics": {"date": self._phys_prac_date, "total": self._phys_prac_total, "mark": round_decimal(self._phys_prac_mark, 1),
                            "percent": phys_prac, "weighted": phys_prac * 0.15},
                "Chemistry": {"date": self._chem_prac_date, "total": self._chem_prac_total, "mark": round_decimal(self._chem_prac_mark, 1),
                            "percent": chem_prac, "weighted": chem_prac * 0.15}
            },
            "Tests": {
                "Physics": {"date": self._phys_test_date, "total": self._phys_test_total, "mark": round_decimal(self._phys_test_mark, 1),
                            "percent": phys_test, "weighted": phys_test * 0.15},
                "Chemistry": {"date": self._chem_test_date, "total": self._chem_test_total, "mark": round_decimal(self._chem_test_mark, 1),
                              "percent": chem_test, "weighted": chem_test * 0.15}
            },
            "Prelims": {
                "Physics": {"date": self._paper1_date, "total": 200, "mark": round_decimal(self._paper1_mark, 1),
                            "percent": paper1, "weighted": paper1 * 0.20},
                "Chemistry": {"date": self._paper2_date, "total": 200, "mark": round_decimal(self._paper2_mark, 1),
                              "percent": paper2, "weighted": paper2 * 0.20}
            },
            "Total": phys_prac*0.15 + chem_prac*0.15 + phys_test*0.15 + chem_test*0.15 + paper1*0.20 + paper2*0.20
        }