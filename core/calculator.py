import bisect
from decimal import Decimal, ROUND_HALF_EVEN

from core.constants import SubjectID


def round_decimal(value: float, places: int = 0) -> float:
    quantizer = Decimal("1." + "0" * places)
    return float(Decimal(str(value)).quantize(quantizer, rounding=ROUND_HALF_EVEN))


def calculate_percentage(mark: float, total: float) -> float:
    if mark < 0 or total < 0:
        raise ValueError(f"Mark and total must be non-negative, got mark={mark}, total={total}")
    elif mark > total:
        raise ValueError(f"Mark cannot exceed total, got mark={mark}, total={total}")
    if total == 0:
        return 0.0
    return (mark / total) * 100


SYMBOL_TABLE = {
    7: {'label': 'A',  'letter': 'A', 'descriptor': 'Outstanding Achievement', 'range': '80% – 100%'},
    6: {'label': 'B',  'letter': 'B', 'descriptor': 'Meritorious Achievement', 'range': '70% – 79%'},
    5: {'label': 'C',  'letter': 'C', 'descriptor': 'Substantial Achievement', 'range': '60% – 69%'},
    4: {'label': 'D',  'letter': 'D', 'descriptor': 'Adequate Achievement',    'range': '50% – 59%'},
    3: {'label': 'E',  'letter': 'E', 'descriptor': 'Moderate Achievement',    'range': '40% – 49%'},
    2: {'label': 'F',  'letter': 'F', 'descriptor': 'Elementary Achievement',  'range': '30% – 39%'},
    1: {'label': 'FF', 'letter': 'G', 'descriptor': 'Not Achieved (Fail)',     'range': '0% – 29%'},
}


def assign_symbol(percentage: float, as_dict: bool = False) -> int | dict:
    thresholds = [30, 40, 50, 60, 70, 80]
    values     = [1, 2, 3, 4, 5, 6, 7]
    level      = values[bisect.bisect_left(thresholds, percentage)]
    if as_dict: return SYMBOL_TABLE[level]
    else: return level



#Generic calculator for all subjects.
def calc_subject(subject_id: int, test_id: int, mark: float, total: int) -> tuple[float, float]:
    from core.subjects import SUBJECT_CHOICES
    percentage = calculate_percentage(mark, total)
    choices = SUBJECT_CHOICES.get(subject_id, {}).get('choices', [])  # ← add .get('choices', [])
    weight = next((w for tid, _, w in choices if tid == test_id), 0.0)
    weighted = percentage * weight
    return percentage, weighted


# ── Individual subject helpers (kept for backward compatibility) ──────────────

def calc_accounting(test_id, mark, total):
    return calc_subject(SubjectID.Accounting, test_id, mark, total)

def calc_agricultural_management(test_id, mark, total):
    return calc_subject(SubjectID.AgriculturalManagement, test_id, mark, total)

def calc_agricultural_sciences(test_id, mark, total):
    return calc_subject(SubjectID.AgriculturalSciences, test_id, mark, total)

def calc_business(test_id, mark, total):
    return calc_subject(SubjectID.Business, test_id, mark, total)

def calc_cat(test_id, mark, total):
    return calc_subject(SubjectID.CAT, test_id, mark, total)

def calc_design(test_id, mark, total):
    return calc_subject(SubjectID.Design, test_id, mark, total)

def calc_dramatic_arts(test_id, mark, total):
    return calc_subject(SubjectID.DramaticArts, test_id, mark, total)

def calc_economics(test_id, mark, total):
    return calc_subject(SubjectID.Economics, test_id, mark, total)

def calc_eng_hl(test_id, mark, total):
    return calc_subject(SubjectID.EngHL, test_id, mark, total)

def calc_fal(test_id, mark, total):
    return calc_subject(SubjectID.FAL, test_id, mark, total)

def calc_geography(test_id, mark, total):
    return calc_subject(SubjectID.Geography, test_id, mark, total)

def calc_history(test_id, mark, total):
    return calc_subject(SubjectID.History, test_id, mark, total)

def calc_it(test_id, mark, total):
    return calc_subject(SubjectID.IT, test_id, mark, total)

def calc_life_orientation(test_id, mark, total):
    return calc_subject(SubjectID.LifeOrientation, test_id, mark, total)

def calc_life_sciences(test_id, mark, total):
    return calc_subject(SubjectID.LifeSciences, test_id, mark, total)

def calc_mathematics(test_id, mark, total):
    return calc_subject(SubjectID.Mathematics, test_id, mark, total)

def calc_other_hl(test_id, mark, total):
    return calc_subject(SubjectID.OtherHL, test_id, mark, total)

def calc_physical_sciences(test_id, mark, total):
    return calc_subject(SubjectID.PhysicalSciences, test_id, mark, total)

def calc_visual_arts(test_id, mark, total):
    return calc_subject(SubjectID.VisualArts, test_id, mark, total)

def cal_maths_lit(test_id, mark, total):
    return calc_subject(SubjectID.MathsLit, test_id, mark, total)