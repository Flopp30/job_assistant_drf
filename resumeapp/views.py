from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from resumeapp.models import Employment, Schedule, KeySkill, LanguageLevel, Language, Resume, Experience
from resumeapp.serializers import ScheduleModelSerializer, SkillModelSerializer, \
    LanguageLevelModelSerializer, LanguageModelSerializer, ResumeModelSerializer, ExperienceModelSerializer


class ScheduleModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer


class SkillModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = KeySkill.objects.all()
    serializer_class = SkillModelSerializer


class LanguageLevelModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = LanguageLevel.objects.all()
    serializer_class = LanguageLevelModelSerializer


class LanguageModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer


class ResumeModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class ExperienceModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
