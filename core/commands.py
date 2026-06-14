import csv
import os
from core.subjects import SUBJECTS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCHOOLS_CSV = os.path.join(BASE_DIR, 'static', 'IEB Schools.csv')

def load_initial_data(sender, **kwargs):
    from portfolio_marker.models import Subject, Schools

    for subject_id, subject_name in SUBJECTS.items():
        Subject.objects.get_or_create(id=subject_id, defaults={'subject': subject_name})

    if not os.path.exists(SCHOOLS_CSV):
        print(f'⚠️  Schools CSV not found at {SCHOOLS_CSV}')
        return

    with open(SCHOOLS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Schools.objects.get_or_create(center_number=row['center_number'], defaults={'name_of_school': row['name_of_school']})