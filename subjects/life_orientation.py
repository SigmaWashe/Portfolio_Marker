from core.calculator import round_decimal, calculate_percentage, assign_symbol


class LifeOrientation:

    def __init__(self, catA_part1: float = 0, catA_part2: float = 0, pe: float = 0, community_service: float = 0,
                 task1_desc: str = "", task1: float = 0, task2_desc: str = "", task2: float = 0):
        self._catA_part1 = catA_part1
        self._catA_part2 = catA_part2
        self._pe = pe
        self._community_service = community_service
        self._task1_desc = task1_desc
        self._task1 = task1
        self._task2_desc = task2_desc
        self._task2 = task2

    def markbreakdown(self):
        return {
            "cat_a":{"part1": round_decimal(self._catA_part1, 1), "part2": round_decimal(self._catA_part2, 1),
                    "mark": round_decimal(self._catA_part1+self._catA_part2, 1)},
            "pe": round_decimal(self._pe, 1), "community_service": round_decimal(self._community_service, 1),
            "task1": {"desc": self._task1_desc, "mark":round_decimal(self._task1, 1)},
            "task2": {"desc": self._task2_desc, "mark":round_decimal(self._task2, 1)},
            "total": round_decimal(self._catA_part1+self._catA_part2+self._pe+self._community_service+self._task1+self._task2, 1)
        }