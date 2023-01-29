"""Module docstrings?"""
from django.db import models

from userapp.models import CustomBaseModel, CustomUser


class Employment(CustomBaseModel):
    """"Модель вида занятости (стажировка, частичная занятость, полная занятость и другие)."""
    """Line 10 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    name = models.CharField(unique=True, verbose_name='Вид занятости', max_length=50)  # Название вида занятости

    class Meta:
        verbose_name = 'Вид занятости'
        verbose_name_plural = 'Виды занятости'

    def __str__(self):
        return self.name


class Schedule(CustomBaseModel):
    """"Модель графика работы (полный день, удаленка, гибкий график и другие)."""
    """Line 23 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    name = models.CharField(unique=True, verbose_name='Тип графика', max_length=50)  # Название вида графика работы

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    def __str__(self):
        return self.name


class KeySkill(CustomBaseModel):
    """"Модель навыков пользователя (Docker, git, Python и другие)."""
    """Line 36 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    name = models.CharField(unique=True, verbose_name='Название навыка', max_length=25)  # Название навыка

    class Meta:
        verbose_name = 'Ключевые навыки'
        verbose_name_plural = 'Ключевые навыки'

    def __str__(self):
        return self.name


class Resume(CustomBaseModel):
    """"Модель резюме пользователя."""
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь',
                             on_delete=models.CASCADE,
                             related_name='resumes')  # Пользователь, подавший резюме
    # Информация о желаемой позиции
    """Line 53, 54, 55 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    professional_role = models.CharField(max_length=150, verbose_name='Должность')  # Позиция на работе/проекте
    employment = models.ManyToManyField(Employment, verbose_name='Вид занятости')  # Вид занятости (стажировка)
    schedule = models.ManyToManyField(Schedule, verbose_name='График работы')  # График работы (полный день, стажировка)
    key_skills = models.ManyToManyField(KeySkill, verbose_name='Клчюевые навыки')  # Навыки
    # Доп информация
    about = models.TextField(verbose_name='Обо мне')  # Доп информация о человеке

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return self.user.email


class Experience(CustomBaseModel):
    """"Модель опыта работы пользователя. Например, места прошлых работ, сделанных проектов"""
    resume = models.ForeignKey(Resume, verbose_name='Резюме', related_name='experiences',
                               on_delete=models.CASCADE)  # Резюме, к которому привязан опыт
    name = models.CharField(verbose_name='Название предыдущего места работы', max_length=50)  # Название работы/проекта
    professional_role = models.CharField(max_length=150, verbose_name='Должность')  # Позиция на работе/проекте
    description = models.TextField(verbose_name='Описание',
                                   blank=True)  # Описание прошлого опыта (что делал на проекте, чем занимался)
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')  # Дата начала работы
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания',
                                       blank=True)  # Дата окончания работы (либо по текущий момент)
    """Line 72, 73, 75, 76 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    # TODO поправить автоназначение started_at и finished_at
    class Meta:
        verbose_name = 'Предыдущее место работы'
        verbose_name_plural = 'Предыдущие места работы'

    def __str__(self):
        return self.name


class LanguageLevel(CustomBaseModel):
    """"Модель уровня владения языком (A2, B1, C1, родной и другие)."""
    name = models.CharField(unique=True, verbose_name='Уровень владения',
                            max_length=25)  # Название уровня владения языком

    class Meta:
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровни владения языком'

    def __str__(self):
        return self.name


class Language(CustomBaseModel):
    """"Модель языка (Английский, Русский и другие)."""
    name = models.CharField(unique=True, verbose_name='Язык', max_length=25)  # Название языка

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class ResumeLanguageLevel(CustomBaseModel):
    """"Модель уровня языка пользователя (Английский, Русский и другие)."""
    resume = models.ForeignKey(Resume, verbose_name='Резюме', on_delete=models.CASCADE,
                               related_name='resumeLanguageLevels')  # Пользователь, подавший резюме
    language = models.ForeignKey(Language, verbose_name='Название языка', on_delete=models.CASCADE,
                                 related_name='userLanguages')  # Уровень владения языком
    """Line 121 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    level = models.ForeignKey(LanguageLevel, verbose_name='Уровень владения', on_delete=models.CASCADE,
                              related_name='userLevels')  # Уровень владения языком

    class Meta:
        verbose_name = 'Язык пользователя'
        verbose_name_plural = 'Языки пользователя'
