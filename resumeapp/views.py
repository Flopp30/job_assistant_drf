"""Module docstrings?"""
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin

from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience
from resumeapp.serializers import (
    ScheduleModelSerializer, KeySkillModelSerializer, ResumeModelSerializer,
    ExperienceModelSerializer, EmploymentModelSerializer
)


class EmploymentModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Employment.objects.all()
    serializer_class = EmploymentModelSerializer


class ScheduleModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer


class SkillModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = KeySkill.objects.all()
    serializer_class = KeySkillModelSerializer


class ResumeModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class ExperienceModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
