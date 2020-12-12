from allauth.account.adapter import DefaultAccountAdapter
from core.models import MyProfile

class UserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):

        user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
        user.save()
        MyProfile.objects.get_or_create(owner=user)
