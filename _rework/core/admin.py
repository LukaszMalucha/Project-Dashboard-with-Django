from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib import admin

from core import models, models_charity, models_project


# USER

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    list_filter = ("is_active", "is_superuser")
    search_fields = ["email", "name"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)


class MyProfileModelAdmin(admin.ModelAdmin):
    """Displaying MyProfile in Admin Panel"""
    list_display = ["owner", "position", "personality", "image"]

    class Meta:
        model = models.MyProfile

    list_filter = (
        "position", "personality"
    )


# CHARITY

class CharityModelAdmin(admin.ModelAdmin):
    """Displaying Charity in Admin Panel"""
    ordering = ["name"]
    list_display = ["name", "description"]

    class Meta:
        model = models_charity.CharityModel


class DonationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models_charity.DonationModel

    list_filter = (
        "donor", "charity__name"
    )


# PROJECTS


class ProjectModelAdmin(admin.ModelAdmin):
    """Displaying Projects in Admin Panel"""
    ordering = ["name"]
    list_display = ["name", "phase", "proposed_by", "budget", "id"]

    class Meta:
        model = models_project.ProjectModel


class IssueModelAdmin(admin.ModelAdmin):
    """Displaying Issues in Admin Panel"""
    list_display = ["name", "project", "cost", "assigned_to"]

    list_filter = (
        "project",
    )

    class Meta:
        model = models_project.IssueModel


class TeamRequirementsModelAdmin(admin.ModelAdmin):
    """Displaying Skillset List in Admin Panel"""
    list_display = ["project", "html", "css", "js", "db", "python"]

    class Meta:
        model = models_project.TeamRequirementsModel


class TeamMembershipModelAdmin(admin.ModelAdmin):
    """Displaying Team Membership in Admin Panel"""
    list_display = ["project", "member", "committed_skill"]

    search_fields = ["project", "member", "committed_skill"]

    class Meta:
        model = models_project.TeamMembershipModel


class ProjectMessageModelAdmin(admin.ModelAdmin):
    """Displaying Project Messages in Admin Panel"""
    list_display = ["project", "message_date", "message"]
    # change_list_template = "admin/project_message_summary_change_list.html"
    date_hierarchy = "message_date"
    search_fields = ["message"]
    list_filter = (
        "project",
    )


class GamificationAdviceModelAdmin(admin.ModelAdmin):
    """Displaying Gamification Advices in Admin Panel"""
    list_display = ["name", "advice"]

    class Meta:
        model = models_project.GamificationAdviceModel


admin.site.register(models.User, UserAdmin)
admin.site.register(models.MyProfile, MyProfileModelAdmin)
admin.site.register(models.Personality)

admin.site.register(models_charity.CharityModel, CharityModelAdmin)
admin.site.register(models_charity.DonationModel, DonationModelAdmin)

admin.site.register(models_project.ProjectModel, ProjectModelAdmin)

admin.site.register(models_project.IssueModel, IssueModelAdmin)
admin.site.register(models_project.TeamRequirementsModel, TeamRequirementsModelAdmin)
admin.site.register(models_project.TeamMembershipModel, TeamMembershipModelAdmin)
admin.site.register(models_project.ProjectMessageModel, ProjectMessageModelAdmin)
admin.site.register(models_project.GamificationAdviceModel, GamificationAdviceModelAdmin)
