from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

NULLABLE = {'blank': True, 'null': True}


class CustomBaseModel(models.Model):
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
    email = models.EmailField(unique=True, verbose_name='Email')
    birthday_date = models.DateTimeField(**NULLABLE, verbose_name='Birthday date')

# TODO: описать сущность резюме после утверждения формы хранения и отображения
# class Resume(CustomBaseModel):
#     user = models.ManyToManyField(CustomUser, verbose_name='User')
