from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from core.utils import schedule_file_name
from django.shortcuts import get_object_or_404
from core.models import MyProfile, User

PHASE_CHOICES = (("proposed", "proposed"),
                 ("analysis", "analysis"),
                 ("development", "development"),
                 ("testing", "testing"),
                 ("deployment", "deployment")
                 )

SKILL_CHOICES = (("html", "html"),
                 ("css", "css"),
                 ("js", "js"),
                 ("db", "db"),
                 ("python", "python")
                 )


class ProjectModel(models.Model):
    """Project Details"""
    name = models.CharField(max_length=254, default="")
    description = models.TextField(blank=False)
    phase = models.CharField(max_length=254, default="proposed", choices=PHASE_CHOICES)
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.IntegerField(default=450, validators=[MinValueValidator(0), MaxValueValidator(450)])
    image_schedule = models.ImageField(upload_to=schedule_file_name, default="schedules/default.jpg")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if self.budget < 0:
            self.phase = "on hold"
            ProjectMessageModel.objects.create(project=self,
                                           message=f"Project '{self.name}' was placed on hold."
                                           ).save()
        super(ProjectModel, self).save(*args, **kwargs)
        profile = get_object_or_404(MyProfile, owner=self.proposed_by)
        profile.my_wallet -= 450
        profile.save()
        TeamRequirementsModel.objects.get_or_create(project=self)
        ProjectMessageModel.objects.get_or_create(
            project=self,
            message=f"Project {self.name} successfully proposed by PM {self.proposed_by}"
        )

    def __str__(self):
        return self.name


class IssueModel(models.Model):
    """Bugs & Issues"""
    name = models.CharField(max_length=254, default="")
    description = models.TextField(blank=False)
    cost = models.IntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(450)])
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee = models.CharField(max_length=254, default="none")

    def get_email(self):
        user = get_object_or_404(User, id=self.assigned_to.id)
        return user.email

    def save(self, *args, **kwargs):
        self.assignee = self.get_email()
        project = get_object_or_404(ProjectModel, id=self.project.id)
        project.budget -= self.cost
        # if project.budget < 0:
        #     project.phase = "on hold"
        #     ProjectMessageModel.objects.create(project=project,
        #                                        message=f"Project '{project.name}' was placed on hold."
        #                                        ).save()
        project.save()
        super(IssueModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project Issue"
        verbose_name_plural = "Projects Issues"

    def __str__(self):
        return "{0}-{1}".format(self.project.name, self.name)


class TeamRequirementsModel(models.Model):
    """Project Skillset Requirement"""
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    python = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    html = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    js = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    css = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    db = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Team Requirements"
        verbose_name_plural = "Team Requirements"

    def __str__(self):
        return str(self.project)


class TeamMembershipModel(models.Model):
    """Team Membership"""
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    committed_skill = models.CharField(max_length=254, default="html", choices=SKILL_CHOICES)
    member_name = models.CharField(max_length=254, default="none")
    member_portrait = models.CharField(max_length=254, default="none")
    member_personality = models.CharField(max_length=254, default="none")

    def get_portrait(self):
        my_profile = get_object_or_404(MyProfile, id=self.member.id)
        return my_profile.image.url

    def get_name(self):
        user = get_object_or_404(User, id=self.member.id)
        return user.name

    def get_personality(self):
        my_profile = get_object_or_404(MyProfile, id=self.member.id)
        return my_profile.personality

    class Meta:
        verbose_name = "Team Membership"
        verbose_name_plural = "Team Memberships"

    def save(self, *args, **kwargs):
        self.member_portrait = self.get_portrait()
        self.member_name = self.get_name()
        self.member_personality = self.get_personality()
        super(TeamMembershipModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.project.name) + " " + str(self.member) + " " + str(self.committed_skill)


class ProjectMessageModel(models.Model):
    """Project Logs"""
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Message"
        verbose_name_plural = "Projects Messages"

    def __str__(self):
        return str(self.project)


class GamificationAdviceModel(models.Model):
    """Gamification advice for Team Composition"""
    name = models.CharField(max_length=254, default="advice")
    advice = models.TextField(blank=False)

    class Meta:
        verbose_name = "Team Gamification Advice"
        verbose_name_plural = "Team Gamification Advices"

    def __str__(self):
        return str(self.name)
