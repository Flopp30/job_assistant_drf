from rest_framework.serializers import ModelSerializer
from resumeapp.models import Employment, Schedule, KeySkill, Resume, Experience
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



class ResumeModelSerializer(ModelSerializer):
    schedule = ScheduleModelSerializer(many=True)
    employment = EmploymentModelSerializer(many=True)
    user = CustomUserModelSerializer()
    key_skills = KeySkillModelSerializer(many=True)
    class Meta:
        model = Resume
        fields = '__all__'


class ExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'