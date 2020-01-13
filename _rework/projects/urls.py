from django.urls import path, include
from projects import views
from rest_framework.routers import DefaultRouter

app_name = 'projects'
router = DefaultRouter()
router.register('projects', views.ProjectModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('team-requirements/<int:pk>/', views.TeamRequirementsViews.as_view(), name="team-requirements")
]
