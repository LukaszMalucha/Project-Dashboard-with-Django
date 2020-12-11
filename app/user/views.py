from core import models
from core import models_project
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from user.utils import compile_profile, personality_test

from .forms import MyProfileForm, PersonalityForm


class CurrentUserView(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            return Response({"email": request.user.email })
        else:
            return Response({"error": "Anonymous"})




@login_required
def profile(request):
    context = compile_profile(request.user)
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):

    my_profile = get_object_or_404(models.MyProfile, owner=request.user)
    positions = ['Coder', 'PM']

    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES, instance=my_profile)

        # Amount of credits depends on user's position
        if form.is_valid():
            if my_profile.position == "PM" and my_profile.my_wallet == 0:
                my_profile.my_wallet = 500
            elif my_profile.position == "Coder" and my_profile.my_wallet == 0:
                my_profile.my_wallet = 100
            else:
                my_profile.my_wallet = my_profile.my_wallet
            my_profile.save()

            return redirect(reverse('user:profile'))

    return render(request, 'edit_profile.html', {'my_profile': my_profile, 'positions': positions})


@login_required
def gamification_test(request):
    my_profile = get_object_or_404(models.MyProfile, owner=request.user)
    form = PersonalityForm(request.POST)
    if my_profile.personality == "":
        if request.method == 'POST':
            answers_list = [request.POST.get('question_1'), request.POST.get('question_2'), request.POST.get('question_3'),
                            request.POST.get('question_4'), request.POST.get('question_5'), request.POST.get('question_6')]
            my_profile.personality = personality_test(answers_list)
            my_profile.save()

            return redirect(reverse('user:profile'))

        return render(request, 'gamification_test.html', {'form': form})

    else:
        return redirect(reverse('user:profile'))


@login_required
def issue_fixed(request, pk):
    issue = get_object_or_404(models_project.IssueModel, id=pk)
    my_profile = get_object_or_404(models.MyProfile, owner=request.user)

    if issue.assigned_to == request.user:
        # reward
        my_profile.my_wallet = my_profile.my_wallet + issue.cost
        my_profile.save()
        issue.delete()

        models_project.ProjectMessageModel.objects.create(
            project=issue.project,
            message='Issue "{0}" fixed by user {1}'.format(issue.name, issue.assigned_to)).save()

        return redirect(reverse('user:profile'))
    return redirect(reverse('user:profile'))