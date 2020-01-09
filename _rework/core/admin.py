from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib import admin


from core import models


# USER

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ('is_active', 'is_superuser')
    search_fields = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)


class MyProfileModelAdmin(admin.ModelAdmin):
    """Displaying MyProfile in Admin Panel"""
    list_display = ["owner", "position", "personality","image"]

    class Meta:
        model = models.MyProfile

    list_filter = (
        "position", "personality"
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.MyProfile, MyProfileModelAdmin)
admin.site.register(models.Personality)
admin.site.register(models.Position)
