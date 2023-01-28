from rest_framework.serializers import ModelSerializer
from resumeapp.models import ProfessionalRole, Employment, Schedule, Skill, LanguageLevel, Language, Resume, Experience


class ProfessionalRoleModelSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalRole
        fields = '__all__'


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
        model = Skill
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