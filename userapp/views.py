from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from userapp.models import CustomUser
from userapp.serializers import CustomUserModelSerializer


class CustomUserModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
