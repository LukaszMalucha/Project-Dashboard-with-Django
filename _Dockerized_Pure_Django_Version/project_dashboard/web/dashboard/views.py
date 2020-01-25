from django.shortcuts import render, get_object_or_404
from core.models_project import Project, Issue
from core.models import MyProfile


def dashboard(request):

    profiles = MyProfile.objects.all()
    projects = Project.objects.all()
    issue_count = len(Issue.objects.all())
    project_count = len(projects)

    context = {'projects': projects, 'profiles': profiles, 'project_count': project_count,
               'issue_count': issue_count }

    return render(request, "dashboard.html", context)


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
