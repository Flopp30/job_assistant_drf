from django.core.management.base import BaseCommand

from constant import (
    EMPLOYMENT_LIST, SCHEDULE_LIST,
    SKILL_LIST, LANGUAGE_LEVEL_LIST,
    LANGUAGES_LIST, CURRENCY_DICT
)
from resumeapp.models import (
    Employment, Schedule, KeySkill,
    LanguageLevel, Language,
)
from vacancyapp.models import Currency


def fill_constant():
    '''
    Заполнение тестовыми данными таблицы:
    - Employment
    - Schedule
    - Skill
    - LanguageLevel
    - Language
    - Currency
    '''

    Employment.objects.all().delete()
    for el in EMPLOYMENT_LIST:
        Employment.objects.create(name=el)

    Schedule.objects.all().delete()
    for el in SCHEDULE_LIST:
        Schedule.objects.create(name=el)

    KeySkill.objects.all().delete()
    for el in SKILL_LIST:
        KeySkill.objects.create(name=el)

    Language.objects.all().delete()
    for language in LANGUAGES_LIST:
        Language.objects.create(name=language)

    LanguageLevel.objects.all().delete()
    for lang_level in LANGUAGE_LEVEL_LIST:
        LanguageLevel.objects.create(name=lang_level)

    Currency.objects.all().delete()
    for key, value in CURRENCY_DICT.items():
        Currency.objects.create(short_name=key, name=value)


class Command(BaseCommand):

    def handle(self, *args, **options):
        fill_constant()
