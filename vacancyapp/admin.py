from django.contrib import admin
from userapp.admin import MarkAsDeletedMixin
from vacancyapp.models import Currency, Vacancy


@admin.register(Currency)
class UserAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'short_name', 'created_at', 'updated_at', 'deleted')
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name')
    list_per_page = 20
    search_fields = ('name', 'short_name',)
    actions = ('mark_as_delete', 'mark_as_active',)
    list_display_links = ('name', 'short_name')


@admin.register(Vacancy)
class UserAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'area_name', 'salary_from', 'salary_to', 'currency',
        'is_active', 'published_hh_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted', 'updated_at', 'currency', 'is_active', 'salary_from', 'salary_to')
    ordering = ('-created_at', 'area_name')
    list_per_page = 20
    search_fields = ('name', 'area_name',)
    actions = ('mark_as_delete', 'mark_as_active',)
    list_display_links = ('name', 'published_hh_at')
