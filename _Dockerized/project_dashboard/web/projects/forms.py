from django import forms
from core.models_project import Project, Issue, RequiredSkills, ProjectPhase, CommitSkill


class ProposeProjectForm(forms.ModelForm):
    """NEW PROJECT"""

    class Meta:
        model = Project
        fields = ['name', 'description', 'image']


class ReportIssueForm(forms.ModelForm):
    """NEW ISSUE"""

    class Meta:
        model = Issue
        fields = ['name', 'description', 'cost']


class RequiredSkillsForm(forms.ModelForm):
    """REQUIRED SKILLS FOR PROJECT"""

    class Meta:
        model = RequiredSkills
        exclude = ['project']


class CommitSkillForm(forms.Form):
    """APPLY FOR A PROJECT TEAM """

    CHOICES = [('html', 'html'),
               ('css', 'css'),
               ('js', 'js'),
               ('db', 'db'),
               ('python', 'python')]

    skill = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


class ChangePhaseForm(forms.ModelForm):
    """ADVANCE PROJECT TO THE NEW STAGE"""

    class Meta:
        model = Project
        fields = ['phase']



