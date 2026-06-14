from core.constants import *
from core.calculator import *


from subjects import (accounting, agricultural_management, agricultural_science, business, computer_application_technology,
                      design, drama, economics, eng_hl, first_additional_language, geography, history, information_technology,
                      life_sciences, mathematics, physical_sciences, visual_art, other_hl, math_lit)

# Icons for the subjects
SUBJECT_CHOICES = {
    SubjectID.Accounting:             {"icon": "calculator",             "choices": Accounting.CHOICES, },
    SubjectID.AgriculturalManagement: {"icon": "tractor",                "choices": AgriculturalManagement.CHOICES, },
    SubjectID.AgriculturalSciences:   {"icon": "tractor",                "choices": AgriculturalSciences.CHOICES, },
    SubjectID.Business:               {"icon": "briefcase",              "choices": Business.CHOICES, },
    SubjectID.CAT:                    {"icon": "monitor",                "choices": CAT.CHOICES, },
    SubjectID.Design:                 {"icon": "house",                  "choices": Design.CHOICES, },
    SubjectID.DramaticArts:           {"icon": "drama",                  "choices": DramaticArts.CHOICES, },
    SubjectID.Economics:              {"icon": "chart-no-axes-combined", "choices": Economics.CHOICES, },
    SubjectID.EngHL:                  {"icon": "book-open",              "choices": EngHL.CHOICES, },
    SubjectID.FAL:                    {"icon": "message-square",         "choices": FAL.CHOICES, },
    SubjectID.Geography:              {"icon": "globe",                  "choices": Geography.CHOICES, },
    SubjectID.History:                {"icon": "landmark",               "choices": History.CHOICES, },
    SubjectID.IT:                     {"icon": "binary",                 "choices": IT.CHOICES, },
    SubjectID.LifeSciences:           {"icon": "dna",                    "choices": LifeSciences.CHOICES, },
    SubjectID.Mathematics:            {"icon": "calculator",             "choices": Mathematics.CHOICES, },
    SubjectID.PhysicalSciences:       {"icon": "flask-conical",          "choices": PhysicalSciences.CHOICES, },
    SubjectID.VisualArts:             {"icon": "palette",                "choices": VisualArt.CHOICES, },
    SubjectID.OtherHL:                {"icon": "languages",              "choices": OtherHL.CHOICES, },
    SubjectID.LifeOrientation:        {"icon": "heart-handshake",        "choices": LifeOrientation.CHOICES, },
    SubjectID.MathsLit:               {"icon": "calculator",             "choices": MathsLit.CHOICES, },
}


# List of subjects
SUBJECTS = {
    SubjectID.Accounting:             'Accounting',
    SubjectID.AgriculturalManagement: 'Agricultural Management',
    SubjectID.AgriculturalSciences:   'Agricultural Sciences',
    SubjectID.Business:               'Business Studies',
    SubjectID.CAT:                    'Computer Applications Technology',
    SubjectID.Design:                 'Design',
    SubjectID.DramaticArts:           'Dramatic Arts',
    SubjectID.Economics:              'Economics',
    SubjectID.EngHL:                  'English Home Language',
    SubjectID.FAL:                    'First Additional Language',
    SubjectID.Geography:              'Geography',
    SubjectID.History:                'History',
    SubjectID.IT:                     'Information Technology',
    SubjectID.LifeSciences:           'Life Sciences',
    SubjectID.Mathematics:            'Mathematics',
    SubjectID.PhysicalSciences:       'Physical Sciences',
    SubjectID.VisualArts:             'Visual Arts',
    SubjectID.OtherHL:                'Other Home Language',
    SubjectID.LifeOrientation:        'Life Orientation',
    SubjectID.MathsLit:               'Mathematical Literacy',
}


# Subjects calculations
SUBJECT_CALC = {
    SubjectID.Accounting:             calc_accounting,
    SubjectID.AgriculturalManagement: calc_agricultural_management,
    SubjectID.AgriculturalSciences:   calc_agricultural_sciences,
    SubjectID.Business:               calc_business,
    SubjectID.CAT:                    calc_cat,
    SubjectID.Design:                 calc_design,
    SubjectID.DramaticArts:           calc_dramatic_arts,
    SubjectID.Economics:              calc_economics,
    SubjectID.EngHL:                  calc_eng_hl,
    SubjectID.FAL:                    calc_fal,
    SubjectID.Geography:              calc_geography,
    SubjectID.History:                calc_history,
    SubjectID.IT:                     calc_it,
    SubjectID.LifeSciences:           calc_life_sciences,
    SubjectID.Mathematics:            calc_mathematics,
    SubjectID.PhysicalSciences:       calc_physical_sciences,
    SubjectID.VisualArts:             calc_visual_arts,
    SubjectID.OtherHL:                calc_other_hl,
    SubjectID.LifeOrientation:        calc_life_orientation,
    SubjectID.MathsLit:               cal_maths_lit,
}


SUBJECT_FIELDS = {
    SubjectID.Accounting:             'accounting',
    SubjectID.AgriculturalManagement: 'agricultural_management',
    SubjectID.AgriculturalSciences:   'agricultural_sciences',
    SubjectID.Business:               'business',
    SubjectID.CAT:                    'cat',
    SubjectID.Design:                 'design',
    SubjectID.DramaticArts:           'dramatic_arts',
    SubjectID.Economics:              'economics',
    SubjectID.EngHL:                  'eng_hl',
    SubjectID.FAL:                    'fal',
    SubjectID.Geography:              'geography',
    SubjectID.History:                'history',
    SubjectID.IT:                     'information_technology',
    SubjectID.LifeSciences:           'life_sciences',
    SubjectID.Mathematics:            'mathematics',
    SubjectID.PhysicalSciences:       'physical_sciences',
    SubjectID.VisualArts:             'visual_arts',
    SubjectID.OtherHL:                'other_hl',
    SubjectID.LifeOrientation:        'life_orientation',
    SubjectID.MathsLit:               'maths_lit',
}


REPORT_TEMPLATES = {
    SubjectID.Accounting:             "Accounting.docx",
    SubjectID.AgriculturalManagement: "AgriculturalManagement.docx",
    SubjectID.AgriculturalSciences:   "Agricultural Sciences.docx",
    SubjectID.Business:               "Business Studies.docx",
    SubjectID.CAT:                    "Computer Applications Technology.docx",
    SubjectID.Design:                 "DESIGN.docx",
    SubjectID.DramaticArts:           "Dramatic Arts.docx",
    SubjectID.Economics:              "Economics.docx",
    SubjectID.EngHL:                  "English Home Language.docx",
    SubjectID.FAL:                    "FIRST ADDITIONAL LANGUAGE.docx",
    SubjectID.Geography:              "Geography.docx",
    SubjectID.History:                "HISTORY.docx",
    SubjectID.IT:                     "Information Technology.docx",
    SubjectID.LifeSciences:           "Life Sciences.docx",
    SubjectID.Mathematics:            "MATHEMATICS.docx",
    SubjectID.PhysicalSciences:       "Physical Sciences.docx",
    SubjectID.VisualArts:             "Visual Arts.docx",
    SubjectID.OtherHL:                "AFRICAN HOME LANGUAGES.docx",
    SubjectID.MathsLit:               "MATHEMATICAL LITERACY.docx"
}

BUILDERS = {
    SubjectID.Accounting:             accounting.build_data,
    SubjectID.AgriculturalManagement: agricultural_management.build_data,
    SubjectID.AgriculturalSciences:   agricultural_science.build_data,
    SubjectID.Business:               business.build_data,
    SubjectID.CAT:                    computer_application_technology.build_data,
    SubjectID.Design:                 design.build_data,
    SubjectID.DramaticArts:           drama.build_data,
    SubjectID.Economics:              economics.build_data,
    SubjectID.EngHL:                  eng_hl.build_data,
    SubjectID.FAL:                    first_additional_language.build_data,
    SubjectID.Geography:              geography.build_data,
    SubjectID.History:                history.build_data,
    SubjectID.IT:                     information_technology.build_data,
    SubjectID.LifeSciences:           life_sciences.build_data,
    SubjectID.Mathematics:            mathematics.build_data,
    SubjectID.PhysicalSciences:       physical_sciences.build_data,
    SubjectID.VisualArts:             visual_art.build_data,
    SubjectID.OtherHL:                other_hl.build_data,
    SubjectID.MathsLit:               math_lit.build_data,
}