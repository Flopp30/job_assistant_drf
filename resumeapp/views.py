"""Module docstrings?"""
from rest_framework.viewsets import GenericViewSet
"""Line 4 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin

from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience
from resumeapp.serializers import (
    ScheduleModelSerializer, KeySkillModelSerializer, ResumeModelSerializer,
    ExperienceModelSerializer, EmploymentModelSerializer
)

"""Line 12 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class EmploymentModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Employment.objects.all()
    serializer_class = EmploymentModelSerializer

"""Line 17 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class ScheduleModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer

"""Line 24 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class SkillModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = KeySkill.objects.all()
    serializer_class = KeySkillModelSerializer

"""Line 30 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class ResumeModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer

"""Line 36 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class ExperienceModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
"""Too many ancestors 9/7 for classes. Maybe refactor?"""
