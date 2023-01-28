from django.contrib import admin
from resumeapp.models import (
    ProfessionalRole, Employment, Schedule, Skill,
    Language, LanguageLevel, Resume, Experience
)
from userapp.admin import MarkAsDeletedMixin


@admin.register(ProfessionalRole)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Employment)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Schedule)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Skill)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(LanguageLevel)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Language)
class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'name', 'level', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


# @admin.register(Resume)
# class ProfessionalRoleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
#     list_display = (
#         'name', 'created_at', 'updated_at', 'deleted'
#     )
#     list_filter = ('deleted',)
#     ordering = ('-created_at', 'name',)
#     list_per_page = 50
#     search_fields = ('name',)
#     actions = ('mark_as_delete', 'mark_as_active')
#     list_display_links = ('name',)
