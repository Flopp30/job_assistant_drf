from uuid import uuid4

from django.db import models

from userapp.models import CustomBaseModel, CustomUser


class ProfessionalRole(CustomBaseModel):
    """" Модель позиции (должности) человека на работе/проекте."""

    name = models.CharField(unique=True, verbose_name='Name', max_length=50)  # Название должности


class Employment(CustomBaseModel):
    """"Модель вида занятости (стажировка, частичная занятость, полная занятость и другие)."""

    name = models.CharField(unique=True, verbose_name='Name',
                            max_length=50)  # Название вида занятости


class Schedule(CustomBaseModel):
    """"Модель графика работы (полный день, удаленка, гибкий график и другие)."""
    name = models.CharField(unique=True, verbose_name='Name',
                            max_length=50)  # Название вида графика работы


class Skill(CustomBaseModel):
    """"Модель навыков пользователя (Docker, git, Python и другие)."""
    name = models.CharField(unique=True, verbose_name='Name', max_length=25)  # Название навыка


class LanguageLevel(CustomBaseModel):
    """"Модель уровня владения языком (A2, B1, C1, родной и другие)."""
    name = models.CharField(unique=True, verbose_name='Name',
                            max_length=25)  # Название уровня владения языком


class Language(CustomBaseModel):
    """"Модель языка (Английский, Русский и другие)."""
    name = models.CharField(unique=True, verbose_name='Name', max_length=25)  # Название языка
    level = models.ForeignKey(LanguageLevel, verbose_name='Language level',
                              on_delete=models.PROTECT)  # Уровень владения языком


class Resume(CustomBaseModel):
    """"Модель резюме пользователя."""
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.CASCADE)  # Пользователь, подавший резюме
    # Информация о желаемой позиции
    professional_roles = models.ManyToManyField(ProfessionalRole,
                                                verbose_name='Position')  # Желаемая позиция (начальник, повар)
    employment = models.ManyToManyField(Employment, verbose_name='Employment')  # Вид занятости (стажировка)
    schedule = models.ManyToManyField(Schedule, verbose_name='Work schedule')  # График работы (полный день, стажировка)
    # Навыки
    languages = models.ManyToManyField(Language, verbose_name='Language')  # Язык
    key_skills = models.ManyToManyField(Skill, verbose_name='Skills')  # Навыки
    # Доп информация
    about = models.TextField(verbose_name='About me')  # Доп информация о человеке


class Experience(CustomBaseModel):
    """"Модель опыта работы пользователя. Например места прошлых работ, сделанных проектов"""
    resume = models.ForeignKey(Resume, verbose_name='Resume', related_name='experiences',
                               on_delete=models.CASCADE)  # Резюме, к которому привязан опыт
    name = models.CharField(verbose_name='Name', max_length=50)  # Название работы/проекта
    professional_roles = models.ForeignKey(ProfessionalRole, verbose_name='Position',
                                           on_delete=models.PROTECT)  # Позиция на работе/проекте
    description = models.TextField(verbose_name='Description',
                                   blank=True)  # Описание прошлого опыта (что делал на проекте, чем занимался)
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Started')  # Дата начала работы
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Finished',
                                       blank=True)  # Дата окончания работы (либо по текущий момент)
