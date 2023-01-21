import json
from django.conf import settings
from django.core.management.base import BaseCommand

from userapp.models import CustomUser


def load_from_json(file_name):
    with open(f'{settings.JSON_DIR}/{file_name}.json', 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = load_from_json('users')
        CustomUser.objects.all().delete()
        for user in users:
            CustomUser.objects.create_user(**user)

        CustomUser.objects.create_superuser('admin', password='admin', email='admin@django.local')
