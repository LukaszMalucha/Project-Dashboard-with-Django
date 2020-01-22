from django.urls import path, include
from charity import views
from rest_framework.routers import DefaultRouter

app_name = 'charity'

router = DefaultRouter()
router.register('charities', views.CharityViewSet, basename="charities")


urlpatterns = [
    path('donate/', views.DonateView.as_view(), name="donate"),
    path('', include(router.urls))
    ]