"""Module docstring?"""
from django.contrib import admin
from resumeapp.models import (
    Employment, Schedule, KeySkill, Resume, Experience, ResumeLanguageLevel, Language, LanguageLevel
)
from userapp.admin import MarkAsDeletedMixin


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
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
class ScheduleAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(KeySkill)
class SkillAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'user',
        'about', 'created_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('created_at',)
    list_per_page = 50
    search_fields = ('about', 'user')
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('user', 'about')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'resume', 'name',
        'description', 'started_at', 'finished_at',
        'created_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('name', 'created_at',)
    list_per_page = 50
    search_fields = ('name', 'description')
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
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
class LanguageAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    """Class docstring?"""
    list_display = (
        'name', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(ResumeLanguageLevel)
class LanguageAdmin(admin.ModelAdmin, MarkAsDeletedMixin):  # Class already defined at line 97.
    """Class docstring?"""
    list_display = (
        'resume', 'language', 'level'
    )
