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
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class ScheduleModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Schedule
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class KeySkillModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = KeySkill
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class LanguageLevelModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = LanguageLevel
        fields = 'name',


class LanguageModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Language
        fields = 'name',


class ResumeLanguageLevelModelSerializer(ModelSerializer):
    """Class docstring?"""
    language = LanguageModelSerializer()
    level = LanguageLevelModelSerializer()

    class Meta:
        """Class docstring?"""
        model = ResumeLanguageLevel
        exclude = 'created_at', 'updated_at', 'deleted', 'id', 'resume'


class ExperienceModelSerializer(ModelSerializer):
    """Class docstring?"""
    class Meta:
        """Class docstring?"""
        model = Experience
        exclude = 'created_at', 'updated_at', 'deleted', 'id', 'resume'


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
