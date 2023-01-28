from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from vacancyapp.models import Currency, Vacancy
from vacancyapp.serializers import CurrencyModelSerializer, VacancyModelSerializer


class CurrencyModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Currency.objects.all()
    serializer_class = CurrencyModelSerializer


class VacancyModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer