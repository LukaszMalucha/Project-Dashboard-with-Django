from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path("current-user/", views.CurrentUserView.as_view(), name="current-user"),

]

