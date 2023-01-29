"""Module docstring?"""
from rest_framework.serializers import ModelSerializer
from userapp.models import CustomUser
from resumeapp.models import LanguageLevel, Language


class CustomUserModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = CustomUser
        # fields = '__all__'
        exclude = 'id',  # Trailing comma tuple.


class LanguageLevelModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = LanguageLevel
        fields = '__all__'


class LanguageModelSerializer(ModelSerializer):
    """Class docstring?"""
    # level = LanguageLevelModelSerializer()
    class Meta:
        """Class docstring?"""
        model = Language
        fields = '__all__'
