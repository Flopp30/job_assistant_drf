from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

NULLABLE = {'blank': True, 'null': True}


class CustomBaseModel(models.Model):
    """Измененная базовая модель. Используй её для создания всех новых моделей."""

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created', editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated', editable=False)
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    class Meta:
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()


class CustomUser(AbstractUser, CustomBaseModel):
    """Измененная модель пользователя."""

    email = models.EmailField(primary_key=True, unique=True, verbose_name='Email')
    birthday_date = models.DateField(**NULLABLE, verbose_name='Birthday date')


class ProfessionalRole(CustomBaseModel):
    """"Модель позиции (должности) человека на работе/проекте."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=50)


class Employment(CustomBaseModel):
    """"Модель вида занятости (стажировка, частичная занятость, полная занятость и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=50)


class Schedule(CustomBaseModel):
    """"Модель графика работы (полный день, удаленка, гибкий график и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=50)


class Skill(CustomBaseModel):
    """"Модель навыков пользователя (Docker, git, Python и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=25)


class LanguageLevel(CustomBaseModel):
    """"Модель уровня владения языком (A2, B1, C1, родной и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=25)


class Language(CustomBaseModel):
    """"Модель языка (Английский, Русский и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=25)
    level = models.ForeignKey(LanguageLevel, verbose_name='Language level', on_delete=models.PROTECT)


class Resume(CustomBaseModel):
    """"Модель резюме пользователя."""

    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.CASCADE)
    # Информация о желаемой позиции
    professional_roles = models.ManyToManyField(ProfessionalRole, verbose_name='Position')
    employment = models.ManyToManyField(Employment, verbose_name='Employment')
    schedule = models.ManyToManyField(Schedule, verbose_name='Work schedule')
    # Навыки
    languages = models.ManyToManyField(Language, verbose_name='Language')
    key_skills = models.ManyToManyField(Skill, verbose_name='Skills')
    # Доп информация
    about = models.TextField(verbose_name='About me')


class Experience(CustomBaseModel):
    """"Модель опыта работы пользователя. Например места прошлых работ, сделанных проектов"""

    resume = models.ForeignKey(Resume, verbose_name='Resume', related_name='experiences', on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, verbose_name='Name', max_length=50)
    professional_roles = models.ForeignKey(ProfessionalRole, verbose_name='Position', on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Description', blank=True)
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Started')
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Finished', blank=True)


# Блок вакансий

class Сurrency(CustomBaseModel):
    """"Модель денежных валют (рубли, доллары и другие)."""

    name = models.CharField(primary_key=True, unique=True, verbose_name='Name', max_length=25)
    short_name = models.CharField(unique=True, verbose_name='Short name', max_length=10)


class Vacancy(CustomBaseModel):
    """"Модель вакансии, созданной работодателем."""

    # Информация о вакансии
    vacancy_hh_id = models.PositiveIntegerField(primary_key=True, verbose_name='ID vacancy')
    name = models.CharField(verbose_name='Name', max_length=50)
    description = models.TextField(verbose_name='Description', blank=True)
    area_name = models.CharField(verbose_name='Location', max_length=150)
    # Деньги
    salary_from = models.PositiveIntegerField(verbose_name='Salary from', default=0)
    salary_to = models.PositiveIntegerField(verbose_name='Salary to', default=0)
    currency = models.ForeignKey(Сurrency, verbose_name='Currency', related_name='vacancys', default=1, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(verbose_name='Active')
    # Требования к кандидату
    candidate_experience_months = models.PositiveIntegerField(verbose_name="Candidate's experience (months)", default=0)
    schedule = models.ManyToManyField(Schedule, verbose_name='Work schedule')
    employment = models.ManyToManyField(Employment, verbose_name='Employment')
    branded_description = models.TextField(verbose_name='Description', blank=True)
    key_skills = models.ManyToManyField(Skill, verbose_name='Skills')
    professional_roles = models.CharField(verbose_name='Professional roles', max_length=50)
    languages = models.ManyToManyField(Language, verbose_name='Language')
    # Техническая информация
    response_url = models.CharField(verbose_name='Response URL', max_length=250, blank=True)
    published_hh_at = models.DateTimeField(verbose_name='Published on hh at')
    created_hh_at = models.DateTimeField(verbose_name='Created on hh at')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

