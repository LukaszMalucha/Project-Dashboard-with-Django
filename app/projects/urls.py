from django.urls import path, include
from projects import views
from rest_framework.routers import DefaultRouter

app_name = 'projects'
router = DefaultRouter()
router.register('projects', views.ProjectModelViewSet, basename="projects")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/team-requirements/', views.TeamRequirementsViews.as_view(), name="team-requirements"),
    path('<int:pk>/project-phase/', views.ProjectPhaseViews.as_view(), name="project-phase"),
    path('<int:pk>/project-complete/', views.CompleteProjectView.as_view(), name="project-complete"),
    path('<int:pk>/team-join/', views.TeamJoinView.as_view(), name="project-team"),
    path('<int:pk>/team-reject/<int:id>/', views.TeamRejectView.as_view(), name="team-reject"),
    path('<int:pk>/issue-create/', views.IssueCreateView.as_view(), name="issue-create"),
    path('issues/<int:id>/issue-assign/', views.IssueAssignView.as_view(), name="issue-assign"),
    path('issues/<int:id>/issue-fixed/', views.IssueFixedView.as_view(), name="issue-fixed"),
    path('issue-count/', views.IssueCountView.as_view(), name="issue-count")
]
