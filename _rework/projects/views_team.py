# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.urls import reverse
#
# from core.models_project import Project, RequiredSkills, CommitSkill, TeamMember
# from .forms import CommitSkillForm
#
#
#
#
#
#
# @login_required
# def join_team(request, pk):
#     """APPLY FOR PROJECT TEAM"""
#     project = Project.objects.get(pk=pk)
#     TeamMember.join_team(request.user, project)
#     requiredskills = get_object_or_404(RequiredSkills, project=project)
#     form = CommitSkillForm(request.POST)
#
#     skill_coverage = CommitSkill.objects.filter(project=project, user=request.user)
#     if skill_coverage:
#         messages.error(request, "Already applied for a Team")
#         return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
#
#
#     if request.method == 'POST':
#
#         if form.is_valid():
#             skill = form.cleaned_data['skill']
#             CommitSkill.objects.create(
#                 project=project,
#                 user=request.user,
#                 skill=skill
#             ).save()
#
#         return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
#
#     return render(request, 'project_team.html', {'form': form, 'requiredskills': requiredskills})
#
#
# @login_required
# def leave_team(request, pk):
#     """REMOVE FROM THE PROJECT TEAM"""
#
#     project = Project.objects.get(pk=pk)
#     commitskill = CommitSkill.objects.filter(project=project)
#     TeamMember.leave_team(request.user, project)
#
#     if request.method == 'POST':
#         user = request.POST['user']
#         commitskill = CommitSkill.objects.filter(project=project, id=user)
#         commitskill.delete()
#
#         return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
#
#     context = {'commitskill':commitskill}
#
#
#     return render(request, 'leave_team.html', context )