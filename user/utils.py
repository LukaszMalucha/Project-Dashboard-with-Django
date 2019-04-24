from django.shortcuts import get_object_or_404

from core import models, models_project


def compile_profile(user):
    """compile user profile for the view"""
    issues = models_project.Issue.objects.filter(assigned_to=user)
    projects = models_project.Project.objects.filter(proposed_by=user)
    # handling empty joined_projects
    try:
        joined_teams = get_object_or_404(models_project.TeamMember,
                                         current_user=user)
        joined_projects = joined_teams.projects.all()
    except:
        joined_projects = []

    personalities = models.Personality.objects.all()
    positions = models.Position.objects.all()
    my_profile = get_object_or_404(models.MyProfile, owner=user)

    context = {'user': user, 'projects': projects, 'issues': issues,
               'my_profile': my_profile, 'personalities': personalities,
               'positions': positions, 'joined_projects': joined_projects}

    return context


def personality_test(answers_list):
    score = 0

    for element in answers_list:  ## score counter
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
        personality = 'socializer'
    elif 11 < score <= 15:
        personality = 'explorer'
    elif 15 < score <= 20:
        personality = 'achiever'
    else:
        personality = 'killer'

    return personality
