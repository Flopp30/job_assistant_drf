from rest_framework.serializers import ModelSerializer
from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience, LanguageLevel, Language, \
    ResumeLanguageLevel
from userapp.serializers import CustomUserModelSerializer


class EmploymentModelSerializer(ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class ScheduleModelSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class KeySkillModelSerializer(ModelSerializer):
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


class ResumeLanguageLevelModelSerializer(ModelSerializer):
    language = LanguageModelSerializer()
    level = LanguageLevelModelSerializer()

    class Meta:
        model = ResumeLanguageLevel
        fields = '__all__'


class ExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


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
