from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404

from core.models import MyProfile
from core.models_project import Project, ProjectMessage, ProjectPhase, RequiredSkills, Issue, TeamMember, CommitSkill
from .forms import ProposeProjectForm, RequiredSkillsForm, ChangePhaseForm
from .utils import project_prize, team_composition


@login_required
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    issues = Issue.objects.filter(project=project)
    my_profile = MyProfile.objects.filter(owner=request.user).first()
    project_owner = MyProfile.objects.filter(owner=project.proposed_by).first()
    profiles = MyProfile.objects.all()
    requiredskills = RequiredSkills.objects.filter(project=project)
    project_team = TeamMember.objects.filter(projects=project)
    skill_coverage = CommitSkill.objects.filter(project=project)
    project_log = ProjectMessage.objects.filter(project=project).order_by('-message_date')
    gamification_dict = team_composition(project_team)
    data_dict = {'project': project, 'my_profile': my_profile, 'profiles': profiles, 'project_log': project_log,
                 'issues': issues, 'requiredskills': requiredskills, 'project_owner': project_owner,
                 'skill_coverage': skill_coverage}
    context = {**gamification_dict, **data_dict}

    return render(request, "project_details.html", context)


@login_required
def propose_project(request):
    my_profile = get_object_or_404(MyProfile, owner=request.user)

    # does not allow to start project without budget needed
    if my_profile.my_wallet < 450:
        messages.error(request, "Insufficient Funds to start a New Project")
        return redirect(reverse('dashboard:dashboard'))

    else:

        if request.method == 'POST':

            form = ProposeProjectForm(request.POST, request.FILES)

            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                budget = 450
                image = form.cleaned_data['image']
                proposed_by = request.user

                new_project = Project.objects.create(
                    name=name,
                    description=description,
                    budget=budget,
                    image=image,
                    proposed_by=proposed_by
                )
                new_project.save()

                # calculate remaining leancoins
                my_profile.my_wallet = my_profile.my_wallet - 450  # calculate remaining leancoins
                my_profile.save()

                RequiredSkills.objects.create(
                    project=new_project
                ).save()

                ProjectMessage.objects.create(
                    project=new_project,
                    message='Project "{0}" proposed by user {1}'.format(new_project.name, new_project.proposed_by)
                ).save()

                return redirect(reverse('dashboard:dashboard'))


        else:
            form = ProposeProjectForm()

    return render(request, 'propose_project.html', {'form': form})

@login_required
def project_skillset(request, pk):
    """DEFINE PROJECT SKILLSET"""
    project = Project.objects.get(id=pk)
    requiredskills = get_object_or_404(RequiredSkills, project=project)


    form = RequiredSkillsForm(request.POST, instance=requiredskills)  # define team skillset needed for project

    if form.is_valid():
        form.save()
        return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
    else:
        form = RequiredSkillsForm(request.POST, instance=requiredskills)

    return render(request, 'project_skillset.html', {'form': form})


@login_required
def advance_project(request, pk):
    """ADVANCE PROJECT TO THE NEW PHASE"""
    if not request.user.is_superuser:
        raise Http404

    project = Project.objects.get(pk=pk)
    project_phases = ProjectPhase.objects.all()

    my_profile = MyProfile.objects.get(owner=project.proposed_by)

    form = ChangePhaseForm(request.POST, instance=project)

    context = {'form': form,
               'project': project,
               'project_phases': project_phases,
               'my_profile': my_profile}

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            ProjectMessage.objects.create(
                project=project,
                message='Project "{0}" advanced to stage "{1}"'.format(project.name, project.phase)
            ).save()

            return redirect(reverse('projects:project_details', kwargs={'pk': pk}))

    return render(request, 'advance_project.html', context)


@login_required
def complete_project(request, pk):
    """FINISH PROJECT"""
    if not request.user.is_superuser:
        raise Http404

    project = Project.objects.get(pk=pk)
    project_team = TeamMember.objects.filter(projects=project)
    project_manager = MyProfile.objects.get(owner=project.proposed_by)

    team_members, prize = project_prize(project, project_team)

    project_manager.my_wallet = project_manager.my_wallet + 540
    project_manager.save()

    for element in project_team:
        user = element.current_user
        winners = MyProfile.objects.filter(owner=user)
        for element in winners:
            element.my_wallet += prize
            element.save()

    project.delete()

    return redirect(reverse('dashboard:dashboard'))


@login_required
def delete_project(request, pk):
    """REMOVE PROJECT"""
    if not request.user.is_superuser:
        raise Http404
    project = get_object_or_404(Project, pk=pk)
    project.delete()

    return redirect(reverse('dashboard:dashboard'))


def find_project(request):

    projects = Project.objects.filter(name__icontains=request.GET['query'])
    profiles = MyProfile.objects.all()
    issue_count = len(Issue.objects.all())
    project_count = len(projects)

    context = {'projects': projects, 'profiles': profiles, 'project_count': project_count,
               'issue_count': issue_count}


    return render(request, "dashboard.html", context)