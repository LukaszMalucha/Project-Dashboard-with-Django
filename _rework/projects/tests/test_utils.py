from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import MyProfile
from core import models_charity, models_project
from projects.utils import team_composition, project_prize


class TeamCompositionTests(TestCase):

    def test_team_composition_1(self):
        project_team = ["explorer", "achiever", "killer"]
        composition = team_composition(project_team)
        self.assertEqual(composition["teamwork_ratio"], -6)
        self.assertEqual(composition["team_type"], "Robot Factory")
        self.assertEqual(composition["statement_1"], "High possibility of Project Fast-Tracking.")
        self.assertEqual(composition["statement_2"], "Slight risk of Scope creep growth.")
        self.assertEqual(composition["statement_3"], "Higher risk of team conflict. Dispute Mediation system required.")

    def test_team_composition_2(self):
        project_team = ["socializer", "socializer", "socializer"]
        composition = team_composition(project_team)
        self.assertEqual(composition["teamwork_ratio"], 6)
        self.assertEqual(composition["team_type"], "Think Tank")
        self.assertEqual(composition["statement_1"],
                        "High Risk of Project Delays and. Increased Timeline monitoring advised. "
                        "Possibility of Project re-scheduling.")
        self.assertEqual(composition["statement_2"], "Regular Brainstorm sessions & Innovation "
                                                     "Incentive setup recommended")
        self.assertEqual(composition["statement_3"], "Slight risk of lower team efficiency due to "
                                                     "increased social activities.")

    def test_team_composition_3(self):
        project_team = ["killer", "socializer", "explorer"]
        composition = team_composition(project_team)
        self.assertEqual(composition["teamwork_ratio"], -2)
        self.assertEqual(composition["team_type"], "Research Lab")
        self.assertEqual(composition["statement_1"], "High Project Budget & Time efficiency.")
        self.assertEqual(composition["statement_2"], "High Project Team Innovation Ratio. "
                                                     "Idea Catcher setup recommended.")
        self.assertEqual(composition["statement_3"], "Implementation of Recognition Programs advised.")

    def test_team_composition_4(self):
        project_team = []
        composition = team_composition(project_team)
        self.assertEqual(composition["teamwork_ratio"], 0)
        self.assertEqual(composition["team_type"], "Equilibrium")
        self.assertEqual(composition["statement_1"], "Project Team Efficiency Ratio is well balanced.")
        self.assertEqual(composition["statement_2"], "Project Team Innovation Ration is well balanced.")
        self.assertEqual(composition["statement_3"], "Project Teamwork Ratio is well balanced.")















