import os

from django.conf import settings
from django.core.management.base import BaseCommand


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



class Command(BaseCommand):

    def handle(self, *args, **options):
        pass
