from django.db import models
from userapp.models import CustomBaseModel
from resumeapp.models import Schedule, Employment, KeySkill, Language, LanguageLevel


class Currency(CustomBaseModel):
    """"Модель денежных валют (рубли, доллары и другие)."""

    name = models.CharField(unique=True, verbose_name='Название валюты', max_length=25)  # Полное название валюты
    short_name = models.CharField(unique=True, verbose_name='Сокращение', max_length=10)  # Короткое название валюты

    class Meta:
        verbose_name = 'Название валюты'
        verbose_name_plural = 'Название валюты'

    def __str__(self):
        return f'{self.name} ({self.short_name})'


class Vacancy(CustomBaseModel):
    """"Модель вакансии, созданной работодателем."""

    # Информация о вакансии
    vacancy_hh_id = models.PositiveIntegerField(verbose_name='ID вакансии на HH')  # ID вакансии
    name = models.CharField(verbose_name='Наименование вакансии', max_length=50)  # Наименование вакансии
    description = models.TextField(verbose_name='Описание вакансии', blank=True)  # Описание вакансии
    area_name = models.CharField(verbose_name='Месторасположение',
                                 max_length=150)  # Месторасположение работы из вакансии
    professional_role = models.CharField(max_length=150, verbose_name='Должность')  # Позиция на работе/проекте
    # Деньги
    salary_from = models.PositiveIntegerField(verbose_name='Зарплата от', default=0)  # Зарплата от
    salary_to = models.PositiveIntegerField(verbose_name='Зарплата до', default=0)  # Зарплата до
    currency = models.ForeignKey(Currency, verbose_name='Вид валюты', related_name='vacancies', default=1,
                                 on_delete=models.SET_DEFAULT)  # Вид валюты
    is_active = models.BooleanField(verbose_name='Активна ли вакансия на агрегаторе?',
                                    default=True)  # Активна ли вакансия
    # Требования к кандидату
    candidate_experience_months = models.PositiveIntegerField(verbose_name="Опыт работы кандидата(months)",
                                                              default=0)  # Опыт работы кандидата (в месяцах)
    schedule = models.ManyToManyField(Schedule, verbose_name='График работы')  # График работы (полный день, полставки)
    employment = models.ManyToManyField(Employment,
                                        verbose_name='Вид работы')  # Вид работы (удаленка, стажировка, офис)
    branded_description = models.TextField(verbose_name='Описание в форамте HTML',
                                           blank=True)  # Описание в форамте HTML
    key_skills = models.ManyToManyField(KeySkill, verbose_name='Требуемые навыки')  # Требуемые навыки от кандидата

    # Техническая информация
    response_url = models.CharField(verbose_name='URL отклика', max_length=250, blank=True)  # URL отклика
    published_hh_at = models.DateTimeField(
        verbose_name='Время публикации вакансии (на hh.ru)')  # Время публикации вакансии (на hh.ru)
    created_hh_at = models.DateTimeField(
        verbose_name='Время создания вакансии (на hh.ru)')  # Время создания вакансии (на hh.ru)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class VacancyLanguageLevel(CustomBaseModel):
    """"Модель уровня языка пользователя (Английский, Русский и другие)."""
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE,
                                related_name='vacancyLanguageLevels')  # Пользователь, подавший резюме
    language = models.ForeignKey(Language, verbose_name='Название языка', on_delete=models.CASCADE,
                                 related_name='vacancyLanguages')  # Уровень владения языком
    level = models.ForeignKey(LanguageLevel, verbose_name='Уровень владения', on_delete=models.CASCADE,
                              related_name='vacancyLevels')  # Уровень владения языком

    class Meta:
        verbose_name = 'Язык вакансии'
        verbose_name_plural = 'Языки вакансии'
