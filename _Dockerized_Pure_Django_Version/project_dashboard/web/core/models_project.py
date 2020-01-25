from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Project(models.Model):
    """Project Details"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField(blank=False)
    phase = models.CharField(max_length=254, default='proposed')
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=6, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = "Project Summary"
        verbose_name_plural = "Projects Summary"

    def __str__(self):
        return self.name


class ProjectPhase(models.Model):
    """Project """
    name = models.CharField(max_length=254, default='proposed')

    class Meta:
        verbose_name = "Project Phase"
        verbose_name_plural = "Projects Phases"

    def __str__(self):
        return self.name


class Issue(models.Model):
    """Bugs & Issues"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField(blank=False)
    cost = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bugs & Issues"
        verbose_name_plural = "Bugs & Issues"

    def __str__(self):
        return "{0}-{1}".format(self.project.name, self.name)


class RequiredSkills(models.Model):
    """Project Skillset Requirement"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    python = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    html = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    js = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    css = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    db = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Required Skillset"
        verbose_name_plural = "Required Skillsets"

    def __str__(self):
        return str(self.project)


class TeamMember(models.Model):
    """Team Membership"""
    projects = models.ManyToManyField(Project)  ## many-to-many relationship
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    @classmethod
    def join_team(cls, current_user, new_project):  ## join team
        teammember, created = cls.objects.get_or_create(
            current_user=current_user
        )
        teammember.projects.add(new_project)

    @classmethod
    def leave_team(cls, current_user, new_project):  ## leave team
        teammember, created = cls.objects.get_or_create(
            current_user=current_user
        )
        teammember.projects.remove(new_project)

    def __str__(self):
        return str(self.current_user)


class CommitSkill(models.Model):
    """Commit Skill to Project Team"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.CharField(max_length=254, default='html')

    class Meta:
        verbose_name = "Skill Coverage"
        verbose_name_plural = "Skills Coverage"

    def __str__(self):
        return "{0}-{1}".format(self.project.name, self.user.name)


class ProjectMessage(models.Model):
    """Project Logs"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project)

class GamificationAdvice(models.Model):
    """Gamification advice for Team Composition"""
    name = models.CharField(max_length=254, default='advice')
    advice = models.TextField(blank=False)

    def __str__(self):
        return str(self.name)