from rest_framework.viewsets import ModelViewSet

from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience
from resumeapp.serializers import (
    ScheduleModelSerializer, KeySkillModelSerializer, ResumeModelSerializer,
    ExperienceModelSerializer, EmploymentModelSerializer
)


class EmploymentModelViewSet(ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentModelSerializer


class ScheduleModelViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer


class SkillModelViewSet(ModelViewSet):
    queryset = KeySkill.objects.all()
    serializer_class = KeySkillModelSerializer


class ResumeModelViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class ExperienceModelViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
