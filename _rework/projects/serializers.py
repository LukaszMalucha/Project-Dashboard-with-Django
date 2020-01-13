from rest_framework import serializers
from core.models import User, MyProfile
from core.models_project import ProjectModel, IssueModel, TeamRequirementsModel


class ProjectModelSerializer(serializers.ModelSerializer):
    """Serializer for project"""

    portrait = serializers.SerializerMethodField('portrait_field')
    pm_name = serializers.SerializerMethodField('pm_name_field')

    def portrait_field(self, obj):
        user = MyProfile.objects.filter(id=obj.proposed_by.id).first()
        return user.image.url

    def pm_name_field(self, obj):
        user = User.objects.filter(id=obj.proposed_by.id).first()
        return user.name

    class Meta:
        model = ProjectModel
        fields = "__all__"
        read_only_fields = ("id", "budget", "phase", "proposed_by", "portrait_field", "pm_name_field")


class TeamRequirementsModelSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Requirements"""

    class Meta:
        model = TeamRequirementsModel
        fields = "__all__"
        read_only_fields = ("project",)

class IssueModelSerializer(serializers.ModelSerializer):
    """Serializer for project issues"""

    class Meta:
        model = IssueModel
        fields = "__all__"
        read_only_fields = ("id",)
