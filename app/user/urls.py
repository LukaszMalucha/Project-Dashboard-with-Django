from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path("current-user/", views.CurrentUserView.as_view(), name="current-user"),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('gamification_test', views.gamification_test, name='gamification_test'),
    path('issue-fixed/<int:pk>', views.issue_fixed, name="issue-fixed"),

]

