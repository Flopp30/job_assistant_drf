import os

from django.core.management.base import BaseCommand

from userapp.models import CustomUser


class Command(BaseCommand):
    ''' Создает суперпользователя admin/admin'''
    def handle(self, *args, **options):
        if os.getenv('ENV_TYPE') == 'local':
            CustomUser.objects.create_superuser('admin', password='admin', email='admin@django.local')
