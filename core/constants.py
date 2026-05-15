SYMBOL_THRESHOLDS = [30, 40, 50, 60, 70, 80]

# -----------------------------------------------------------------------------
# English Home Language  — test_IDs
# -----------------------------------------------------------------------------
class EngHLTest:
    EXT_WRITING  = 1
    CAT = 2
    LITERATURE = 3
    TEST = 4
    PRELIM_PAPER_1 = 5
    PRELIM_PAPER_2 = 6


# -----------------------------------------------------------------------------
# Other Home Language  — test_IDs
# -----------------------------------------------------------------------------
class OtherHLTest:
    EXT_WRITING = 1
    CAT_TASK_1 = 2
    CAT_TASK_2 = 3
    LITERATURE = 4
    TEST = 5
    PRELIM_PAPER_1 = 6
    PRELIM_PAPER_2 = 7


# -----------------------------------------------------------------------------
# First Additional Language  — test_IDs
# -----------------------------------------------------------------------------
class FALTest:
    EXT_WRITING = 1
    CAT = 2
    LITERATURE = 3
    TEST = 4
    PRELIM_PAPER_1 = 5
    PRELIM_PAPER_2 = 6


# -----------------------------------------------------------------------------
# Mathematics  — test_IDs
# -----------------------------------------------------------------------------
class MathematicsTest:
    SHORT_ITEM = 1
    LONG_ITEM = 2
    TEST = 3
    PRELIM_PAPER_1 = 4
    PRELIM_PAPER_2 = 5


# -----------------------------------------------------------------------------
# Life Orientation  — test_IDs
# (marks summed directly, no weighting)
# -----------------------------------------------------------------------------
class LifeOrientationTest:
    CAT_A_PART_1 = 1
    CAT_A_PART_2 = 2
    PE = 3
    COMMUNITY_SERVICE  = 4
    TASK_1 = 5
    TASK_2 = 6


# -----------------------------------------------------------------------------
# Business Studies  — test_IDs
# -----------------------------------------------------------------------------
class BusinessTest:
    TASK = 1
    SECTION_AB = 2
    SECTION_C = 3
    PRELIM = 4


# -----------------------------------------------------------------------------
# Computer Application Technology  — test_IDs
# -----------------------------------------------------------------------------
class CATTest:
    THEORY = 1
    PRAC = 2
    ALT_TEST = 3
    PRELIM_1 = 4
    PRELIM_2 = 5
    PAT = 6


# -----------------------------------------------------------------------------
# Geography  — test_IDs
# -----------------------------------------------------------------------------
class GeographyTest:
    TASK = 1
    RESEARCH = 2
    TEST = 3
    PRELIM_PAPER_1  = 4
    PRELIM_PAPER_2  = 5


# -----------------------------------------------------------------------------
# History  — test_IDs
# -----------------------------------------------------------------------------
class HistoryTest:
    TEST = 1
    PRELIM_PAPER_1 = 2
    PRELIM_PAPER_2 = 3
    HIST_INV = 4
    SOURCE_ANALYSIS = 5
    SOURCE_BASED_ESSAY = 6
    VISUAL_ANALYSIS = 7


# -----------------------------------------------------------------------------
# Information Technology  — test_IDs
# -----------------------------------------------------------------------------
class ITTest:
    PAT = 1
    THEORY = 2
    PRAC = 3
    ALT = 4
    PRELIM_THEORY = 5
    PRELIM_PRAC = 6


# -----------------------------------------------------------------------------
# Life Sciences  — test_IDs
# -----------------------------------------------------------------------------
class LifeSciencesTest:
    PRELIM_PAPER_1 = 1
    PRELIM_PAPER_2 = 2
    TEST = 3
    PRAC = 4
    RESEARCH_PROJECT = 5
    CONTROLLED_WRITING_PIECE = 6
    CASE_STUDY = 7
    SUMMATIVE_PRACTICAL = 8


# -----------------------------------------------------------------------------
# Physical Sciences  — test_IDs
# -----------------------------------------------------------------------------
class PhysicalSciencesTest:
    PHYS_PRAC = 1
    CHEM_PRAC = 2
    PHYS_TEST = 3
    CHEM_TEST = 4
    PRELIM_1 = 5
    PRELIM_2 = 6

class EngHLWeight:
    EXT_WRITING = 0.15
    CAT = 0.50/3
    LITERATURE = 0.20
    TEST = 0.20/3
    PRELIM = 0.40/3

class OtherHLWeight:
    EXT_WRITING = 0.10
    CAT = 0.10
    LITERATURE = 0.20
    TEST = 0.025
    PRELIM = 0.40

class FALWeight:
    EXT_WRITING = 0.15
    CAT = 0.20
    LITERATURE = 0.20
    TEST = 0.1/3
    PRELIM = 0.20

class MathematicsWeight:

    SHORT_ITEM = 0.15
    LONG_ITEM = 0.30
    TEST = 0.10
    PRELIM = 0.20

class LifeOrientationWeight:
    pass

class BusinessWeight:
    PRELIM_TOTAL = 300

    TASK = 0.20
    SECTION = 0.15
    PRELIM = 0.30

class CATWeight:
    PRELIM1_TOTAL = 180
    PRELIM2_TOTAL = 150
    PAT_TOTAL     = 170

    THEORY = 0.175
    PRAC = 0.175
    ALT = 0.15
    PRELIM1 = 0.25
    PRELIM2 = 0.25

class GeographyWeight:
    TASK = 0.15
    RESEARCH = 0.30
    TEST = 0.15
    PRELIM = 0.25

class HistoryWeight:
    TEST = 0.10
    PRELIM = 0.25
    HIST_INV = 0.45
    ALT_TASK = 0.15

class ITWeight:
    PAT = 1
    THEORY = 0.175
    PRAC = 0.175
    ALT = 0.15
    PRELIM = 0.25

class LifeSciencesWeight:
    PRELIM = 0.25
    TEST = 0.15
    TASK = 0.15
    PRAC = 0.15

class PhysicalSciencesWeight:
    PAPER_TOTAL = 200

    INVESTIGATION = 0.15
    TEST = 0.15
    PRELIM = 0.20