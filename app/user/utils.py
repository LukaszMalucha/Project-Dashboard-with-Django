from django.shortcuts import get_object_or_404

from core import models
from core import models_project


def compile_profile(user):
    """compile user profile for the view"""
    my_profile = get_object_or_404(models.MyProfile, owner=user)
    if my_profile.position == "PM":
        position = "Project Manager"
    elif my_profile.position == "admin":
        position = "Program Manager"
    elif my_profile.position == "Coder":
        position = "Coder"
    else:
        position = "guest"

    issues = models_project.IssueModel.objects.filter(assigned_to=user)
    teams = models_project.TeamMembershipModel.objects.filter(member=user)
    projects = models_project.ProjectModel.objects.filter(proposed_by=user)
    joined_teams = models_project.TeamMembershipModel.objects.filter(member=user)

    context = {"user": user, "my_profile": my_profile, "position": position,
               "issues": issues, "teams": teams, "projects": projects, "joined_teams": joined_teams}

    return context


def personality_test(answers_list):
    score = 0

    for element in answers_list:  # score counter
        if element == "answer_1":
            score += 1
        elif element == "answer_2":
            score += 3
        elif element == "answer_3":
            score += 4
        elif element == "answer_4":
            score += 2

    # Score personality
    if score <= 11:
        personality = "socializer"
    elif 11 < score <= 15:
        personality = "explorer"
    elif 15 < score <= 20:
        personality = "achiever"
    else:
        personality = "killer"

    return personality
