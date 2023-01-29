import json
from random import choice, randint

from django.conf import settings
from django.core.management.base import BaseCommand

from constant import ABOUT_ME, PROFESSIONAL_ROLES, DESCRIPTIONS
from resumeapp.models import Employment, Schedule, Language, KeySkill, Resume, LanguageLevel, ResumeLanguageLevel, \
    Experience
from userapp.models import CustomUser


def load_from_json(file_name):
    with open(f'{settings.JSON_DIR}/{file_name}.json', 'r') as json_file:
        return json.load(json_file)


def fill_users():
    '''Заполнение тестовыми данными таблицу пользователей'''
    users = load_from_json('users')
    CustomUser.objects.all().delete()
    for user in users:
        CustomUser.objects.create_user(**user)


def fill_resume():
    users = CustomUser.objects.all()
    employments = Employment.objects.all()
    schedules = Schedule.objects.all()
    languages = Language.objects.all()

    language_levels = LanguageLevel.objects.all()
    key_skills = KeySkill.objects.all()

    Resume.objects.all().delete()
    for about_me, prof_role in zip(ABOUT_ME, PROFESSIONAL_ROLES):
        user = choice(users)
        employment = choice(employments)
        key_skill = choice(key_skills)
        schedule = choice(schedules)

        resume = Resume.objects.create(user=user, professional_role=prof_role, about=about_me)
        n = randint(1, 4)
        for i in range(n):
            language = choice(languages)
            language_level = choice(language_levels)
            ResumeLanguageLevel.objects.create(resume=resume, language=language, level=language_level)
        resume.employment.add(employment)
        resume.schedule.add(schedule)
        resume.key_skills.add(key_skill)


def fill_experience():
    resumes = Resume.objects.all()
    previous_jobs_name = ['ЦИАН', 'EPAM', 'Google', 'Yandex', 'Mail', 'Rambler']
    professional_role = PROFESSIONAL_ROLES
    descriptions = DESCRIPTIONS
    for resume, name, role, desc in zip(resumes, previous_jobs_name, professional_role, descriptions):
        Experience.objects.create(resume=resume, name=name, professional_role=role, description=desc)


class Command(BaseCommand):

    def handle(self, *args, **options):
        fill_users()
        fill_resume()
        fill_experience()
