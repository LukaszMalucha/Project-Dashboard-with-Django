
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.views import IndexTemplateView
from django.views.generic import TemplateView

urlpatterns = [
      path('password-reset/confirm/<str:uidb64>/<str:token>',
              TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
      path('admin/', admin.site.urls),
      path('accounts/', include('allauth.urls')),
      path('auth/', include('dj_rest_auth.urls')),
      path('auth/registration/', include('dj_rest_auth.registration.urls')),
      path('auth/', include('user.urls')),
      path('api/projects/', include('projects.urls')),
      path('charity/', include('charity.urls')),
      re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
