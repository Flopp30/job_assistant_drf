"""Module docstring?"""
from django.contrib import admin

from userapp.models import CustomUser


class MarkAsDeletedMixin:
    """Class docstring?"""
    def mark_as_delete(self, request, queryset):  # Unused argument 'request'.
        """Method docstring?"""
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

    def mark_as_active(self, request, queryset):  # Unused argument 'request'.
        """Method docstring?"""
        queryset.update(deleted=False)

    mark_as_active.short_description = 'Снять пометку на удаление'


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'date_joined', 'last_login'
    )
    """Line 22 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    list_filter = ('is_active', 'is_superuser')
    ordering = ('last_login', 'is_active',)
    list_per_page = 20
    search_fields = ('name_first', 'name_second', 'username', 'email')
    actions = ('mark_as_delete', 'mark_as_active', 'mark_as_superuser', 'mark_as_user')
    list_display_links = ('email', 'username')

    def mark_as_superuser(self, request, queryset):  # Unused argument 'request'.
        """Method docstring?"""
        queryset.update(is_superuser=True)

    mark_as_superuser.short_description = 'Сделать суперпользователем'

    def mark_as_user(self, request, queryset):  # Unused argument 'request'.
        """Method docstring?"""
        queryset.update(is_superuser=False)

    mark_as_user.short_description = 'Сделать обычным пользователем'
