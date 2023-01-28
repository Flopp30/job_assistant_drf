# Generated by Django 4.1.5 on 2023-01-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyapp', '0002_alter_currency_created_at_alter_currency_deleted_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Название валюты', 'verbose_name_plural': 'Название валюты'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='professional_roles',
            field=models.CharField(max_length=150, verbose_name='Должность'),
        ),
    ]