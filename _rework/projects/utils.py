from core.models import MyProfile


def team_composition(project_team):
    """Gamification guide for team composition"""
    achievers = 0
    explorers = 0
    socializers = 0
    killers = 0
    team_profiles = []
    if project_team:
        for element in project_team:
            team_profiles = MyProfile.objects.filter(owner=element.current_user)
            for row in team_profiles:
                if row.personality == "achiever":
                    achievers += 1
                elif row.personality == "explorer":
                    explorers += 1
                elif row.personality == "socializer":
                    socializers += 1
                elif row.personality == "killer":
                    killers += 1
    else:
        pass

    efficiency_ratio = socializers * (-2) + explorers * 1 + killers * 2 + achievers * 3
    innovation_ratio = socializers * (-2) + explorers * 3 + killers * 2 + achievers * 1
    teamwork_ratio = socializers * 2 + explorers * (-2) + killers * (-2) + achievers * (-2)

    if efficiency_ratio > 5:
        statement_1 = "High possibility of Project Fast-Tracking."
    elif 0 < efficiency_ratio <= 5:
        statement_1 = "High Project Budget & Time efficiency."
    elif -5 <= efficiency_ratio < 0:
        statement_1 = "Risk of Project Delays. Increased Team communication advised."
    elif efficiency_ratio < -5:
        statement_1 = "High Risk of Project Delays and. Increased Timeline monitoring advised. Possibility of Project re-scheduling."
    else:
        statement_1 = "Project Team Efficiency Ratio is well balanced."

    if innovation_ratio > 5:
        statement_2 = "Slight risk of Scope creep growth."
    elif 0 < innovation_ratio <= 5:
        statement_2 = "High Project Team Innovation Ratio. Idea Catcher setup recommended."
    elif -5 <= innovation_ratio < 0:
        statement_2 = "Regular Brainstorm sessions recommended."
    elif innovation_ratio < -5:
        statement_2 = "Regular Brainstorm sessions & Innovation Incentive setup recommended"
    else:
        statement_2 = "Project Team Innovation Ration is well balanced."

    if teamwork_ratio > 5:
        statement_3 = "Slight risk of lower team efficiency due to increased social activities."
    elif 0 < teamwork_ratio <= 5:
        statement_3 = "High Project Teamwork Ratio indicator. Standard monitoring practices advised"
    elif -5 <= teamwork_ratio < 0:
        statement_3 = "Implementation of Recognition Programs advised."
    elif teamwork_ratio < -5:
        statement_3 = "Higher risk of team conflict. Dispute Mediation system required."
    else:
        statement_3 = "Project Teamwork Ratio is well balanced."

    project_ratios = [efficiency_ratio, innovation_ratio, teamwork_ratio]

    if max(project_ratios) == efficiency_ratio and efficiency_ratio != 0:
        team_type = "Robot Factory"
    elif max(project_ratios) == innovation_ratio and innovation_ratio != 0:
        team_type = "Research Lab"
    elif max(project_ratios) == teamwork_ratio and teamwork_ratio != 0:
        team_type = "Think Tank"
    else:
        team_type = "Equilibrium"

    gamification_dict = {
        'achievers': achievers,
        'explorers': explorers,
        'socializers': socializers,
        'killers': killers,
        'team_profiles': team_profiles,
        'efficiency_ratio': efficiency_ratio,
        'innovation_ratio': innovation_ratio,
        'teamwork_ratio': teamwork_ratio,
        'team_type': team_type,
        'statement_1': statement_1,
        'statement_2': statement_2,
        'statement_3': statement_3
    }

    return gamification_dict


def project_prize(project, project_team):
    """LeanCoin prize for completing projects"""

    team_members = len(project_team)
    if team_members != 0:
        prize = project.budget / team_members
    else:
        prize = 0

    return team_members, prize
