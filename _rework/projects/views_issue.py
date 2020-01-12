# from django.shortcuts import render,redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse
#
# from core.models import MyProfile
# from core.models_project import Project, ProjectMessage, Issue
# from projects.forms import ReportIssueForm
#
# @login_required
# def report_issue(request, pk):
#     """RAISE NEW ISSUE"""
#
#     form = ReportIssueForm(request.POST)
#
#     if form.is_valid():
#         name = form.cleaned_data['name']
#         description = form.cleaned_data['description']
#         cost = form.cleaned_data['cost']
#         project = Project.objects.get(pk=pk)
#
#         new_issue = Issue.objects.create(
#             name=name,
#             description=description,
#             cost=cost,
#             project=project,
#             assigned_to=request.user)
#         new_issue.save()
#
#         message = ProjectMessage.objects.create(project=project,
#                                                 message='Issue "{0}" raised by pm {1}'.format(new_issue.name,
#                                                                                               new_issue.assigned_to))
#         message.save()
#
#         project.budget = project.budget - new_issue.cost  ## deduct issue cost from project budget
#         if project.budget < 0:
#             project.status = "hold"
#             ProjectMessage.objects.create(
#                 project=project,
#                 message='Project "{0}" placed on hold.'.format(project.name)
#             ).save()
#         project.save()
#         return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
#
#     else:
#         form = ReportIssueForm(request.POST)
#
#     return render(request, 'report_issue.html', {'form': form, })
#
#
# @login_required
# def assign_issue(request, pk, ik):
#     """ASSIGN PROJECT ISSUE TO YOURSELF"""
#
#     issue = get_object_or_404(Issue, id=ik)
#     issue.assigned_to = request.user
#     issue.save()
#
#     ProjectMessage.objects.create(
#         project=issue.project,
#         message='Issue "{0}" assigned to user {1}'.format(issue.name, issue.assigned_to)
#     ).save()
#
#     return redirect(reverse('projects:project_details', kwargs={'pk': pk}))
#
#
# @login_required
# def issue_fixed(request, ik):
#     issue = get_object_or_404(Issue, id=ik)
#     my_profile = get_object_or_404(MyProfile, owner=request.user)
#
#     # reward
#     my_profile.my_wallet = my_profile.my_wallet + issue.cost
#     my_profile.save()
#     issue.delete()
#
#     ProjectMessage.objects.create(
#         project=issue.project,
#         message='Issue "{0}" fixed by user {1}'.format(issue.name, issue.assigned_to)).save()
#
#     return redirect(reverse('user:profile'))
