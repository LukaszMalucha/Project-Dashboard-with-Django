from django.urls import path, include
from projects import views
from rest_framework.routers import DefaultRouter

app_name = 'projects'
router = DefaultRouter()
router.register('projects', views.ProjectModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('team-requirements/<int:pk>/', views.TeamRequirementsViews.as_view(), name="team-requirements"),
    path('project-phase/<int:pk>/', views.ProjectPhaseViews.as_view(), name="project-phase"),
    path('project-complete/<int:pk>/', views.CompleteProjectView.as_view(), name="project-complete"),
    path('team-join/<int:pk>/', views.TeamJoinView.as_view(), name="project-team"),
    path('team-reject/<int:pk>/<int:id>/', views.TeamRejectView.as_view(), name="team-reject")
]
