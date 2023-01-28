from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

NULLABLE = {'blank': True, 'null': True}


class CustomBaseModel(models.Model):
    """Измененная базовая модель. Используй её для создания всех новых моделей."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана: ', editable=False)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено', editable=False)  # Дата обновления
    deleted = models.BooleanField(default=False, verbose_name='Удален?')  # Дата удаления

    class Meta:
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
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.email)


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


class UserLanguageLevel(CustomBaseModel):
    """"Модель уровня языка пользователя (Английский, Русский и другие)."""
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='userLanguageLevels')  # Пользователь, подавший резюме
    language = models.ForeignKey(Language, verbose_name='Название языка', on_delete=models.CASCADE, related_name='userLanguages')  # Уровень владения языком
    level = models.ForeignKey(LanguageLevel, verbose_name='Уровень владения',  on_delete=models.CASCADE, related_name='userLevels')  # Уровень владения языком

    class Meta:
        verbose_name = 'Язык пользователя'
        verbose_name_plural = 'Языки пользователя'
