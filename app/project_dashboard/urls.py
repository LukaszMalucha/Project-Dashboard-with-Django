"""vuebank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.views import IndexTemplateView

urlpatterns = [
      path('admin/', admin.site.urls),
      path('charity/', include('charity.urls')),
      path('user/', include('user.urls')),
      path("user/", include("django.contrib.auth.urls")),
      path("user/", include('allauth.urls')),
      path('api/user/', include('user.api.urls')),
      path('api/projects/', include('projects.urls')),
      re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
