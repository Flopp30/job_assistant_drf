# Generated by Django 4.1.5 on 2023-01-23 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('about', models.TextField(verbose_name='About me')),
                ('employment', models.ManyToManyField(to='userapp.employment', verbose_name='Employment')),
                ('language', models.ManyToManyField(to='userapp.language', verbose_name='Language')),
                ('position', models.ManyToManyField(to='userapp.position', verbose_name='Position')),
                ('schedule', models.ManyToManyField(to='userapp.schedule', verbose_name='Work schedule')),
                ('skill', models.ManyToManyField(to='userapp.skill', verbose_name='Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]