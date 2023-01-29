"""Module docstring?"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
"""Standard import should be placed before django.db..."""

NULLABLE = {'blank': True, 'null': True}


class CustomBaseModel(models.Model):
    """Измененная базовая модель. Используй её для создания всех новых моделей."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана: ', editable=False)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено', editable=False)  # Дата обновления
    """Line 12, 13 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    deleted = models.BooleanField(default=False, verbose_name='Удален?')  # Дата удаления

    class Meta:  # Too few public methods. Refactor?
        """Class docstring?"""
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()


class CustomUser(AbstractUser, CustomBaseModel):
    """Измененная модель пользователя."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name='Email')  # Эл. почта
    birthday_date = models.DateField(**NULLABLE, verbose_name='Дата рождения')  # Дата рождения

    class Meta:
        """Class docstring?"""
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.email)
