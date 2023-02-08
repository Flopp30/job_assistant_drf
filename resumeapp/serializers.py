from rest_framework.serializers import ModelSerializer
from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience, LanguageLevel, Language, \
    ResumeLanguageLevel
from userapp.serializers import CustomUserModelSerializer


class EmploymentModelSerializer(ModelSerializer):
    class Meta:
        model = Employment
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class ScheduleModelSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class KeySkillModelSerializer(ModelSerializer):
    class Meta:
        model = KeySkill
        exclude = 'created_at', 'updated_at', 'deleted', 'id'


class LanguageLevelModelSerializer(ModelSerializer):
    class Meta:
        model = LanguageLevel
        fields = 'name',


class LanguageModelSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = 'name',


class ResumeLanguageLevelModelSerializer(ModelSerializer):
    language = LanguageModelSerializer()
    level = LanguageLevelModelSerializer()

    class Meta:
        model = ResumeLanguageLevel
        exclude = 'created_at', 'updated_at', 'deleted', 'id', 'resume'


class ExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = Experience
        exclude = 'created_at', 'updated_at', 'deleted', 'id', 'resume'


class ResumeModelSerializer(ModelSerializer):
    schedule = ScheduleModelSerializer(many=True)
    employment = EmploymentModelSerializer(many=True)
    user = CustomUserModelSerializer()
    key_skills = KeySkillModelSerializer(many=True)
    resumeLanguageLevels = ResumeLanguageLevelModelSerializer(many=True)
    experiences = ExperienceModelSerializer(many=True)

    class Meta:
        model = Resume
        fields = '__all__'
