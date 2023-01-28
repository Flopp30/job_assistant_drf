from rest_framework.serializers import ModelSerializer
from resumeapp.models import Employment, Schedule, KeySkill, LanguageLevel, Language, Resume, Experience


class EmploymentModelSerializer(ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class ScheduleModelSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class SkillModelSerializer(ModelSerializer):
    class Meta:
        model = KeySkill
        fields = '__all__'


class LanguageLevelModelSerializer(ModelSerializer):
    class Meta:
        model = LanguageLevel
        fields = '__all__'


class LanguageModelSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ResumeModelSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class ExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'