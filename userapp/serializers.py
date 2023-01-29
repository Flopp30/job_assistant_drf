"""Module docstring?"""
from rest_framework.serializers import ModelSerializer
from userapp.models import CustomUser
from resumeapp.models import LanguageLevel, Language


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = 'id',


class LanguageLevelModelSerializer(ModelSerializer):
    class Meta:
        model = LanguageLevel
        fields = '__all__'


class LanguageModelSerializer(ModelSerializer):
    # level = LanguageLevelModelSerializer()
    class Meta:
        model = Language
        fields = '__all__'
