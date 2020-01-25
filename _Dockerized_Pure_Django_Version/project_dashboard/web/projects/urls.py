from django.urls import path
from projects import views_project, views_team, views_issue

app_name = 'projects'

urlpatterns = [
    path('<int:pk>', views_project.project_details, name='project_details'),
    path('propose_project/', views_project.propose_project, name='propose_project'),
    path('<int:pk>/project_skillset', views_project.project_skillset, name='project_skillset'),
    path('<int:pk>/advance_project', views_project.advance_project, name='advance_project'),
    path('<int:pk>/delete_project/', views_project.delete_project, name='delete_project'),
    path('<int:pk>/complete_project/', views_project.complete_project, name='complete_project'),
    path('find_project', views_project.find_project, name="find_project"),
    path('<int:pk>/report_issue/', views_issue.report_issue, name='report_issue'),
    path('<int:pk>/assign_issue/<int:ik>', views_issue.assign_issue, name='assign_issue'),
    path('issue_fixed/<int:ik>', views_issue.issue_fixed, name='issue_fixed'),
    path('<int:pk>/join_team', views_team.join_team, name='join_team'),
    path('<int:pk>/leave_team', views_team.leave_team, name='leave_team')
    ]