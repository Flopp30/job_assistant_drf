from django.db import models
from userapp.models import CustomBaseModel
from resumeapp.models import Schedule, Employment, Skill, Language


class Currency(CustomBaseModel):
    """"Модель денежных валют (рубли, доллары и другие)."""

    name = models.CharField(unique=True, verbose_name='Name', max_length=25)  # Полное название валюты
    short_name = models.CharField(unique=True, verbose_name='Short name', max_length=10)  # Короткое название валюты


class Vacancy(CustomBaseModel):
    """"Модель вакансии, созданной работодателем."""

    # Информация о вакансии
    vacancy_hh_id = models.PositiveIntegerField(verbose_name='ID vacancy')  # ID вакансии
    name = models.CharField(verbose_name='Name', max_length=50)  # Наименование вакансии
    description = models.TextField(verbose_name='Description', blank=True)  # Описание вакансии
    area_name = models.CharField(verbose_name='Location', max_length=150)  # Месторасположение работы из вакансии
    # Деньги
    salary_from = models.PositiveIntegerField(verbose_name='Salary from', default=0)  # Зарплата от
    salary_to = models.PositiveIntegerField(verbose_name='Salary to', default=0)  # Зарплата до
    currency = models.ForeignKey(Currency, verbose_name='Currency', related_name='vacancies', default=1,
                                 on_delete=models.SET_DEFAULT)  # Вид валюты
    is_active = models.BooleanField(verbose_name='Active', default=True)  # Активна ли вакансия
    # Требования к кандидату
    candidate_experience_months = models.PositiveIntegerField(verbose_name="Candidate's experience (months)",
                                                              default=0)  # Опыт работы кандидата (в месяцах)
    schedule = models.ManyToManyField(Schedule, verbose_name='Work schedule')  # График работы (полный день, полставки)
    employment = models.ManyToManyField(Employment,
                                        verbose_name='Employment')  # Вид работы (удаленка, стажировка, офис)
    branded_description = models.TextField(verbose_name='Description', blank=True)  # Описание в форамте HTML
    key_skills = models.ManyToManyField(Skill, verbose_name='Skills')  # Требуемые навыки от кандидата
    professional_roles = models.CharField(verbose_name='Professional roles',
                                          max_length=50)  # Должность (начальник, повар)
    languages = models.ManyToManyField(Language, verbose_name='Language')  # Языки
    # Техническая информация
    response_url = models.CharField(verbose_name='Response URL', max_length=250, blank=True)  # URL отклика
    published_hh_at = models.DateTimeField(verbose_name='Published on hh at')  # Время публикации вакансии (на hh.ru)
    created_hh_at = models.DateTimeField(verbose_name='Created on hh at')  # Время создания вакансии (на hh.ru)
