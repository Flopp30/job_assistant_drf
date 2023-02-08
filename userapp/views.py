from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from userapp.serializers import LanguageLevelModelSerializer, LanguageModelSerializer
from userapp.models import CustomUser
from userapp.serializers import CustomUserModelSerializer
from resumeapp.models import LanguageLevel, Language


class CustomUserModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class LanguageLevelModelViewSet(ModelViewSet):
    serializer_class = LanguageLevelModelSerializer
    queryset = LanguageLevel.objects.all()
    permission_classes = [IsAdminUser, DjangoModelPermissionsOrAnonReadOnly]


class LanguageModelViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
    permission_classes = [IsAdminUser, DjangoModelPermissionsOrAnonReadOnly]

