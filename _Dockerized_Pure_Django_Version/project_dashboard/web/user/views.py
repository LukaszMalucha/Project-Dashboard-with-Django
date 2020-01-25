from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, MyDetailsForm, PersonalityForm
from core import models, models_project, models_charity
from .utils import compile_profile, personality_test


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(email=request.POST['email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('dashboard:dashboard'))
            else:
                messages.error(request, "Your email or password are incorrect")
    else:
        login_form = UserLoginForm()

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                # create default user details
                models.MyProfile.objects.create(position="guest", personality="", my_wallet=0,
                                                owner=request.user).save()
                messages.success(request, "You have successfully registered")
                return redirect(reverse('dashboard:dashboard'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('dashboard:dashboard'))


@login_required
def profile(request):
    context = compile_profile(request.user)

    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):

    my_profile = get_object_or_404(models.MyProfile, owner=request.user)
    positions = models.Position.objects.all()

    if request.method == 'POST':
        form = MyDetailsForm(request.POST, request.FILES, instance=my_profile)

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
    if request.method == 'POST':
        answers_list = [request.POST.get('question_1'), request.POST.get('question_2'), request.POST.get('question_3'),
                        request.POST.get('question_4'), request.POST.get('question_5'), request.POST.get('question_6')]
        my_profile.personality = personality_test(answers_list)
        my_profile.save()

        return redirect(reverse('user:profile'))

    return render(request, 'gamification_test.html', {'form': form})
