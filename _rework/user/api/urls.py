from django.urls import path

from user.api import views

app_name = 'api-user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
    path('my-account/', views.ManageUserView.as_view(), name='my-account')
]

