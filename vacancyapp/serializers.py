from rest_framework.serializers import ModelSerializer

from vacancyapp.models import Currency, Vacancy


class CurrencyModelSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class VacancyModelSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
