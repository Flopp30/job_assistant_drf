from django.contrib import admin
from userapp.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'first_name', 'last_name', 'username', 'email', 'is_active', 'is_superuser', 'date_joined', 'last_login'
    )
    list_filter = ('is_active', 'is_superuser')
    ordering = ('last_login', 'is_active',)
    list_per_page = 20
    search_fields = ('name_first', 'name_second', 'username', 'email')
    actions = ('mark_as_delete', 'mark_as_active', 'mark_as_superuser', 'mark_as_user')

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

    def mark_as_active(self, request, queryset):
        queryset.update(deleted=False)

    mark_as_active.short_description = 'Снять пометку на удаление'

    def mark_as_superuser(self, request, queryset):
        queryset.update(is_superuser=True)

    mark_as_superuser.short_description = 'Сделать суперпользователем'

    def mark_as_user(self, request, queryset):
        queryset.update(is_superuser=False)

    mark_as_user.short_description = 'Сделать обычным пользователем'
