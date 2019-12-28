from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib import admin


from core import models, models_charity, models_project


# USER

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)


class MyProfileModelAdmin(admin.ModelAdmin):
    """Displaying MyProfile in Admin Panel"""
    list_display = ["owner", "position", "personality","image"]

    class Meta:
        model = models.MyProfile

    list_filter = (
        "position", "personality"
    )


# CHARITY

class CharityModelAdmin(admin.ModelAdmin):
    """Displaying Charity in Admin Panel"""
    list_display = ["name","description"]
    class Meta:
        model = models_charity.Charity

class DonationLineAdminInline(admin.TabularInline):
    """Displaying Single Donation in Admin Panel"""
    model = models_charity.DonationLineItem


class DonationModelAdmin(admin.ModelAdmin):
    """Donor & Date display in Admin Panel"""
    inlines = (DonationLineAdminInline,)  # from above
    list_display = ["donor", "date"]
    date_hierarchy = 'date'

    class Meta:
        model = models_charity.Donation


# PROJECTS


class ProjectModelAdmin(admin.ModelAdmin):
    """Displaying Projects in Admin Panel"""
    list_display = ["name", "phase", 'proposed_by', 'budget']

    class Meta:
        model = models_project.Project


class IssueModelAdmin(admin.ModelAdmin):
    """Displaying Issues in Admin Panel"""
    list_display = ["name", "project", "cost", "assigned_to"]

    list_filter = (
        "project",
    )

    class Meta:
        model = models_project.Issue


class RequiredSkillsModelAdmin(admin.ModelAdmin):
    """Displaying Skillset List in Admin Panel"""
    list_display = ["project","html","css","js","db","python"]
    class Meta:
        model = models_project.RequiredSkills


class TeamMemberModelAdmin(admin.ModelAdmin):
    """Displaying Team Membership in Admin Panel"""
    list_display = ["current_user", "user_projects"]

    search_fields = ["current_user", "user_projects"]

    class Meta:
        model = models_project.TeamMember

    def user_projects(self, obj):
        return "\n".join([p.name for p in obj.projects.all()])


class CommitSkillModelAdmin(admin.ModelAdmin):
    """Displaying Team Membership in Admin Panel"""
    list_display = ["project", "user", "skill"]
    search_fields = ["user", "skill"]
    list_filter = (
        "project", "skill"
    )

    class Meta:
        model = models_project.CommitSkill


class ProjectMessageModelAdmin(admin.ModelAdmin):
    """Displaying Project Messages in Admin Panel"""
    list_display = ["project", "message_date", "message"]
    # change_list_template = 'admin/project_message_summary_change_list.html'
    date_hierarchy = 'message_date'
    search_fields = ["message"]
    list_filter = (
        'project',
    )

class GamificationAdviceModelAdmin(admin.ModelAdmin):
    """Displaying Gamification Advices in Admin Panel"""
    list_display = ["name", "advice"]

    class Meta:
        model = models_project.GamificationAdvice






admin.site.register(models.User, UserAdmin)
admin.site.register(models.MyProfile, MyProfileModelAdmin)
admin.site.register(models.Personality)
admin.site.register(models.Position)

admin.site.register(models_charity.Charity, CharityModelAdmin)
admin.site.register(models_charity.Donation, DonationModelAdmin)

admin.site.register(models_project.Project, ProjectModelAdmin)

admin.site.register(models_project.ProjectPhase)
admin.site.register(models_project.Issue, IssueModelAdmin)
admin.site.register(models_project.RequiredSkills, RequiredSkillsModelAdmin)
admin.site.register(models_project.CommitSkill, CommitSkillModelAdmin)
admin.site.register(models_project.ProjectMessage, ProjectMessageModelAdmin)
admin.site.register(models_project.GamificationAdvice, GamificationAdviceModelAdmin)