from django.urls import path
from charity import views

app_name = 'charity'

urlpatterns = [
    path('propose_charity/', views.propose_charity, name='propose_charity'),
    path('delete_charity/<int:pk>', views.delete_charity, name='delete_charity'),
    path('support/<id>', views.add_to_donations, name="add_to_donations"),
    path('adjust/<id>', views.adjust_donations, name="adjust_donations"),
    path('view_donations', views.view_donations, name="view_donations"),
    path('charity_donation/', views.charity_donation, name="charity_donation")

    ]