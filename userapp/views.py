"""Module docstring?"""
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin

from userapp.serializers import LanguageLevelModelSerializer, LanguageModelSerializer
from userapp.models import CustomUser
from userapp.serializers import CustomUserModelSerializer
from resumeapp.models import LanguageLevel, Language


class CustomUserModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class LanguageLevelModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    serializer_class = LanguageLevelModelSerializer
    queryset = LanguageLevel.objects.all()


class LanguageModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
