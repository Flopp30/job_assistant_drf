"""Module docstring?"""
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.viewsets import GenericViewSet
"""Line 3 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from userapp.serializers import LanguageLevelModelSerializer, LanguageModelSerializer
from userapp.models import CustomUser
from userapp.serializers import CustomUserModelSerializer
from resumeapp.models import LanguageLevel, Language


"""Line 11 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
class CustomUserModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    """Class docstring?"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    

class LanguageLevelModelViewSet(ModelViewSet):
    """Class docstring?"""

    serializer_class = LanguageLevelModelSerializer
    queryset = LanguageLevel.objects.all()
    permission_classes = [IsAdminUser, DjangoModelPermissionsOrAnonReadOnly]


class LanguageModelViewSet(ModelViewSet):
    """Class docstring?"""
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
    permission_classes = [IsAdminUser, DjangoModelPermissionsOrAnonReadOnly]


# Classes have too many ancestors 9/7. Refactor maybe?

