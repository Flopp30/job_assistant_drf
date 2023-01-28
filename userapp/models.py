from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

NULLABLE = {'blank': True, 'null': True}


class CustomBaseModel(models.Model):
    """Измененная базовая модель. Используй её для создания всех новых моделей."""

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created', editable=False)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated', editable=False)  # Дата обновления
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted')  # Дата удаления

    class Meta:
        abstract = True

    def delete(self, *args):
        self.is_deleted = True
        self.save()


class CustomUser(AbstractUser, CustomBaseModel):
    """Измененная модель пользователя."""

    email = models.EmailField(primary_key=True, unique=True, verbose_name='Email')  # Эл. почта
    birthday_date = models.DateField(**NULLABLE, verbose_name='Birthday date')  # Дата рождения


