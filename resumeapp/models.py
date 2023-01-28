from django.db import models

from userapp.models import CustomBaseModel, CustomUser


class Employment(CustomBaseModel):
    """"Модель вида занятости (стажировка, частичная занятость, полная занятость и другие)."""

    name = models.CharField(unique=True, verbose_name='Вид занятости', max_length=50)  # Название вида занятости

    class Meta:
        verbose_name = 'Вид занятости'
        verbose_name_plural = 'Виды занятости'

    def __str__(self):
        return self.name


class Schedule(CustomBaseModel):
    """"Модель графика работы (полный день, удаленка, гибкий график и другие)."""
    name = models.CharField(unique=True, verbose_name='Тип графика', max_length=50)  # Название вида графика работы

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    def __str__(self):
        return self.name


class KeySkill(CustomBaseModel):
    """"Модель навыков пользователя (Docker, git, Python и другие)."""
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

    class Meta:
        verbose_name = 'Предыдущее место работы'
        verbose_name_plural = 'Предыдущие места работы'

    def __str__(self):
        return self.name
