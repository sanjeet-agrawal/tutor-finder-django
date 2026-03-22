import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from tutors.models import Tutor, Subject

fake = Faker()

# Create subjects if not exist
subjects_list = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
subjects = []

for sub in subjects_list:
    subject_obj, created = Subject.objects.get_or_create(name=sub)
    subjects.append(subject_obj)

# Create tutors
for i in range(1000):
    username = fake.user_name()

    user = User.objects.create_user(
        username=username,
        password='password123'
    )

    Tutor.objects.create(
        user=user,
        subject=random.choice(subjects),
        experience=random.randint(1, 10),
        location=fake.city(),
        hourly_rate=random.randint(200, 1000),
        bio=fake.text()
    )

print("✅ 1000 Tutors Created Successfully!")