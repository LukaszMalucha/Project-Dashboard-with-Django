from rest_framework import serializers
from core.models import User, MyProfile
from django.shortcuts import get_object_or_404
from core.models_project import ProjectModel, IssueModel, TeamRequirementsModel, TeamMembershipModel
from django.forms.models import model_to_dict


class ProjectModelSerializer(serializers.ModelSerializer):
    """Serializer for project"""

    portrait = serializers.SerializerMethodField("portrait_field")
    pm_name = serializers.SerializerMethodField("pm_name_field")
    team_requirements = serializers.SerializerMethodField("team_requirements_field")
    team_membership = serializers.SerializerMethodField("team_membership_field")

    def portrait_field(self, obj):
        user = get_object_or_404(MyProfile, id=obj.proposed_by.id)
        return user.image.url

    def pm_name_field(self, obj):
        user = get_object_or_404(User, id=obj.proposed_by.id)
        return user.name

    def team_requirements_field(self, obj):
        team = get_object_or_404(TeamRequirementsModel, project=obj.id)
        team = model_to_dict(team)
        return team
    
    def team_membership_field(self, obj):
        team = TeamMembershipModel.objects.filter(project=obj.id).values()

        return team

    class Meta:
        model = ProjectModel
        fields = "__all__"
        read_only_fields = (
            "id", "budget", "phase", "proposed_by", "portrait_field", "pm_name_field", 
            "team_requirements_field", "team_membership_field")


class TeamRequirementsModelSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Requirements"""

    class Meta:
        model = TeamRequirementsModel
        fields = "__all__"
        read_only_fields = ("project",)


class ProjectPhaseSerializer(serializers.ModelSerializer):
    """Serializer for Project phase"""

    class Meta:
        model = ProjectModel
        fields = ("phase",)


class TeamMembershipModelSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Membership"""

    portrait = serializers.SerializerMethodField("portrait_field")

    def portrait_field(self, obj):
        portrait = obj.get_portrait()
        return portrait

    class Meta:
        model = TeamMembershipModel
        fields = "__all__"


class IssueModelSerializer(serializers.ModelSerializer):
    """Serializer for project issues"""

    class Meta:
        model = IssueModel
        fields = "__all__"
        read_only_fields = ("id",)
