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
class EmploymentAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
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
class SkillAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
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
class LanguageLevelAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
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
    list_display = (
        'name', 'level', 'created_at', 'updated_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('-created_at', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'user',
        'about', 'created_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('professional_roles', 'created_at',)
    list_per_page = 50
    search_fields = ('about', 'user')
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('user', 'about')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin, MarkAsDeletedMixin):
    list_display = (
        'resume', 'name', 'professional_roles',
        'description', 'started_at', 'finished_at',
        'created_at', 'deleted'
    )
    list_filter = ('deleted',)
    ordering = ('name', 'created_at',)
    list_per_page = 50
    search_fields = ('name', 'description')
    actions = ('mark_as_delete', 'mark_as_active')
    list_display_links = ('name',)
