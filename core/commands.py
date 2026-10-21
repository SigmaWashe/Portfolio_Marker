import csv
import os
from core.subjects import SUBJECTS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCHOOLS_CSV = os.path.join(BASE_DIR, 'static', 'IEB Schools.csv')

def load_initial_data(sender, **kwargs):
    from common.models import Subject, Schools

    for subject_id, subject_name in SUBJECTS.items():
        Subject.objects.get_or_create(id=subject_id, defaults={'subject': subject_name})

    if not os.path.exists(SCHOOLS_CSV):
        print(f'⚠️  Schools CSV not found at {SCHOOLS_CSV}')
        return

    with open(SCHOOLS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Schools.objects.get_or_create(center_number=row['center_number'], defaults={'name_of_school': row['name_of_school']})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

"""
def create_superuser():
    username = 'admin'
    password = 'admin123'
    email = 'admin@example.com'
    if User.objects.filter(username=username).exists():
        print('Superuser already exists')
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created successfully')
"""


