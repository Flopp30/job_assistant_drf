"""Module docstrings?"""
from rest_framework.serializers import ModelSerializer
"""Line 4 too long. https://peps.python.org/pep-0008/#maximum-line-length"""
from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience, LanguageLevel, Language, \
    ResumeLanguageLevel
from userapp.serializers import CustomUserModelSerializer


class EmploymentModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:  # Too few public methods. Refactor?
        """Class docstring?"""
        model = Employment
        fields = '__all__'


class ScheduleModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Schedule
        fields = '__all__'


class KeySkillModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = KeySkill
        fields = '__all__'


class LanguageLevelModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = LanguageLevel
        fields = '__all__'


class LanguageModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Language
        fields = '__all__'


class ResumeLanguageLevelModelSerializer(ModelSerializer):
    """Class docstring?"""
    language = LanguageModelSerializer()
    level = LanguageLevelModelSerializer()

    class Meta:
        """Class docstring?"""
        model = ResumeLanguageLevel
        fields = '__all__'


class ExperienceModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Experience
        fields = '__all__'


class ResumeModelSerializer(ModelSerializer):
    """Class docstring?"""
    schedule = ScheduleModelSerializer(many=True)
    employment = EmploymentModelSerializer(many=True)
    user = CustomUserModelSerializer()
    key_skills = KeySkillModelSerializer(many=True)
    resumeLanguageLevels = ResumeLanguageLevelModelSerializer(many=True)
    experiences = ExperienceModelSerializer(many=True)


    class Meta:
        """Class docstring?"""
        model = Resume
        fields = '__all__'
