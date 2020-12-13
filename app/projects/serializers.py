from rest_framework import serializers
from core import models
from django.shortcuts import get_object_or_404
from core import models_project
from django.forms.models import model_to_dict
from rest_framework.exceptions import ValidationError
from projects.utils import team_composition


class ProjectModelSerializer(serializers.ModelSerializer):
    """Serializer for project"""

    portrait = serializers.SerializerMethodField("portrait_field")
    pm_name = serializers.SerializerMethodField("pm_name_field")
    pm_email = serializers.SerializerMethodField("pm_email_field")
    team_requirements = serializers.SerializerMethodField("team_requirements_field")
    team_membership = serializers.SerializerMethodField("team_membership_field")
    project_messages = serializers.SerializerMethodField("project_messages_field")
    project_issues = serializers.SerializerMethodField("project_issues_field")
    project_team_composition = serializers.SerializerMethodField("project_team_composition_field")

    def portrait_field(self, obj):
        user = get_object_or_404(models.MyProfile, id=obj.proposed_by.id)
        return user.image.url

    def pm_name_field(self, obj):
        user = get_object_or_404(models.User, id=obj.proposed_by.id)
        return user.username

    def pm_email_field(self, obj):
        user = get_object_or_404(models.User, id=obj.proposed_by.id)
        return user.email

    def team_requirements_field(self, obj):
        required_team = get_object_or_404(models_project.TeamRequirementsModel, project=obj.id)
        required_team = model_to_dict(required_team)
        return required_team

    def team_membership_field(self, obj):
        team = models_project.TeamMembershipModel.objects.filter(project=obj.id).values()
        return team

    def project_messages_field(self, obj):
        messages = models_project.ProjectMessageModel.objects.filter(project=obj.id).values()
        return messages

    def project_issues_field(self, obj):
        issues = models_project.IssueModel.objects.filter(project=obj.id).values()
        return issues

    def project_team_composition_field(self, obj):
        team = models_project.TeamMembershipModel.objects.values_list("member_personality", flat=True).filter(
            project=obj.id)
        team = team_composition(team)
        return team

    class Meta:
        model = models_project.ProjectModel
        fields = "__all__"
        read_only_fields = (
            "id", "budget", "phase", "proposed_by", "portrait_field", "pm_name_field", "pm_email_field"
                                                                                       "team_requirements_field",
            "team_membership_field", "project_messages_field", "project_issues_field",
            "project_team_composition_field")

    def validate(self, attrs):
        """LeanCoins balance"""
        user = self.context['request'].user
        profile = get_object_or_404(models.MyProfile, owner=user)
        if profile.my_wallet < 450:
            raise ValidationError(f" Your LeanCoin balance ({profile.my_wallet}) is insufficient to start new project")
        return attrs


class TeamRequirementsModelSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Requirements"""

    class Meta:
        model = models_project.TeamRequirementsModel
        fields = "__all__"
        read_only_fields = ("project",)


class ProjectPhaseSerializer(serializers.ModelSerializer):
    """Serializer for Project phase"""

    class Meta:
        model = models_project.ProjectModel
        fields = ("phase",)


class TeamMembershipModelSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Membership"""
    portrait = serializers.SerializerMethodField("portrait_field")

    def portrait_field(self, obj):
        portrait = obj.get_portrait()
        return portrait

    class Meta:
        model = models_project.TeamMembershipModel
        fields = "__all__"
        read_only_fields = ("project", "member", "member_name", "member_portrait", "member_personality")


class TeamRejectionSerializer(serializers.ModelSerializer):
    """Serializer for Project Team Rejection"""

    class Meta:
        model = models_project.TeamMembershipModel
        fields = "__all__"
        read_only_fields = ("project", "member_name", "member_portrait", "committed_skill")


class IssueCreateSerializer(serializers.ModelSerializer):
    """Serializer for project issues"""

    class Meta:
        model = models_project.IssueModel
        fields = "__all__"
        read_only_fields = ("id", "project", "assigned_to")
