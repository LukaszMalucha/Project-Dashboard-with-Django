from django.urls import path, include
from charity import views
from rest_framework.routers import DefaultRouter

app_name = 'charity'
router = DefaultRouter()
router.register('charities', views.CharityViewSet)


urlpatterns = [
    path('charity_donation/', views.charity_donation, name="charity_donation"),
    path('', include(router.urls))
    ]