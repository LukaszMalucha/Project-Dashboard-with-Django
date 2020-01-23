# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from rest_framework.test import APIClient
# from core.models import MyProfile
# from core import models_charity, models_project
# from projects.utils import team_composition, project_prize
#
# def sample_superuser():
#     user = get_user_model().objects.create_superuser(
#         email="superuser@gmail.com",
#         password="test1234",
#     )
#     return user
#
#
# def sample_user():
#     user = get_user_model().objects.create_user(
#         email="user@gmail.com",
#         password="test1234",
#     )
#     return user
#
#
# def sample_project(user):
#     payload = {"name": "Test", "description": "test", "proposed_by": user}
#     project = models_project.ProjectModel.objects.create(**payload)
#     return project
#
#
#
#
# class TeamCompositionTests(TestCase):
#
#     def test_team_composition_1(self):
#         project_team = ["explorer", "achiever", "killer"]
#         composition = team_composition(project_team)
#         self.assertEqual(composition["teamwork_ratio"], -6)
#         self.assertEqual(composition["team_type"], "Robot Factory")
#         self.assertEqual(composition["statement_1"], "High possibility of Project Fast-Tracking.")
#         self.assertEqual(composition["statement_2"], "Slight risk of Scope creep growth.")
#         self.assertEqual(composition["statement_3"], "Higher risk of team conflict. Dispute Mediation system required.")
#
#     def test_team_composition_2(self):
#         project_team = ["socializer", "socializer", "socializer"]
#         composition = team_composition(project_team)
#         self.assertEqual(composition["teamwork_ratio"], 6)
#         self.assertEqual(composition["team_type"], "Think Tank")
#         self.assertEqual(composition["statement_1"], "High Risk of Project Delays and. Increased "
#                                                      "Timeline monitoring advised. Possibility of "
#                                                      "Project re-scheduling.")
#         self.assertEqual(composition["statement_2"], "Regular Brainstorm sessions & Innovation "
#                                                      "Incentive setup recommended.")
#         self.assertEqual(composition["statement_3"], "Slight risk of lower team efficiency due to "
#                                                      "increased social activities.")
#
#     def test_team_composition_3(self):
#         project_team = ["killer", "socializer", "explorer"]
#         composition = team_composition(project_team)
#         self.assertEqual(composition["teamwork_ratio"], -2)
#         self.assertEqual(composition["team_type"], "Research Lab")
#         self.assertEqual(composition["statement_1"], "High Project Budget & Time efficiency.")
#         self.assertEqual(composition["statement_2"], "High Project Team Innovation Ratio. "
#                                                      "Idea Catcher setup recommended.")
#         self.assertEqual(composition["statement_3"], "Implementation of Recognition Programs advised.")
#
#     def test_team_composition_4(self):
#         project_team = []
#         composition = team_composition(project_team)
#         self.assertEqual(composition["teamwork_ratio"], 0)
#         self.assertEqual(composition["team_type"], "Equilibrium")
#         self.assertEqual(composition["statement_1"], "Project Team Efficiency Ratio is well balanced.")
#         self.assertEqual(composition["statement_2"], "Project Team Innovation Ration is well balanced.")
#         self.assertEqual(composition["statement_3"], "Project Teamwork Ratio is well balanced.")
#
#
#     def test_team_composition_5(self):
#         project_team = ["socializer"]
#         composition = team_composition(project_team)
#         self.assertEqual(composition["statement_1"], "Risk of Project Delays. Increased Team communication advised.")
#         self.assertEqual(composition["statement_2"], "Regular Brainstorm sessions recommended.")
#         self.assertEqual(composition["statement_3"], "High Project Teamwork Ratio indicator."
#                                                      " Standard monitoring practices advised.")
#
# class ProjectPrizeTests(TestCase):
#
#     def setUp(self):
#         self.user = sample_user()
#         self.superuser = sample_superuser()
#         self.project = sample_project(self.superuser)
#
#
#
#     def test_project_prize(self):
#
#         project_team = [1,2,3,4]
#         project = self.project
#         prize = project_prize(project, project_team)
#         self.assertEqual(prize, (4, 112))
#
#     def test_project_prize_empty(self):
#
#         project_team = []
#         project = self.project
#         prize = project_prize(project, project_team)
#         self.assertEqual(prize, (0, 0))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
