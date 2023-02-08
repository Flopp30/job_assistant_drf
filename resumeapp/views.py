"""Module docstrings?"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience
from resumeapp.serializers import (
    ScheduleModelSerializer, KeySkillModelSerializer, ResumeModelSerializer,
    ExperienceModelSerializer, EmploymentModelSerializer
)


class EmploymentModelViewSet(ModelViewSet):
    """Class docstring?"""
    queryset = Employment.objects.all()
    serializer_class = EmploymentModelSerializer


class ScheduleModelViewSet(ModelViewSet):
    """Class docstring?"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer


class SkillModelViewSet(ModelViewSet):
    """Class docstring?"""
    queryset = KeySkill.objects.all()
    serializer_class = KeySkillModelSerializer


class ResumeModelViewSet(ModelViewSet):
    """Class docstring?"""
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class ExperienceModelViewSet(ModelViewSet):

"""Line 12 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
"""Too many ancestors 9/7 for classes. Maybe refactor?"""
