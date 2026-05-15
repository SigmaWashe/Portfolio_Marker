import bisect
from decimal import Decimal, ROUND_HALF_EVEN


def round_decimal(value: float, places: int = 0) -> float:
    quantizer = Decimal("1." + "0" * places)
    return float(Decimal(str(value)).quantize(quantizer, rounding=ROUND_HALF_EVEN))

def calculate_percentage(mark: float, total: float) -> float:
    if mark < 0 or total < 0:
        raise ValueError(
            f"Mark and total must be non-negative, got mark={mark}, total={total}"
        )
    elif mark > total:
        raise ValueError(
            f"Mark cannot exceed total, got mark={mark}, total={total}"
        )
    if total == 0:
        return 0.0
    return (mark / total) * 100

_SYMBOL_THRESHOLDS = [30, 40, 50, 60, 70, 80]
_SYMBOL_VALUES     = [ 1,  2,  3,  4,  5,  6, 7]


def assign_symbol(percentage: float) -> int:
    return _SYMBOL_VALUES[bisect.bisect_left(_SYMBOL_THRESHOLDS, percentage)]