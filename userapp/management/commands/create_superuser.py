"""Module docstring?"""
import os

from django.core.management.base import BaseCommand

from userapp.models import CustomUser


class Command(BaseCommand):
    ''' Создает суперпользователя admin/admin'''
    def handle(self, *args, **options):
        if os.getenv('ENV_TYPE') == 'local':
            """Line 14 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
            CustomUser.objects.create_superuser('admin', password='admin', email='admin@django.local')
