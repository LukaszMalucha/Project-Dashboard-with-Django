from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .forms import ProposeCharityForm, DonationForm, MakeDonationForm

from django.contrib.auth.decorators import login_required

from core.models_charity import Charity, DonationLineItem
from core.models import MyProfile
from .forms import ProposeCharityForm
from django.http import Http404
from django.conf import settings
import stripe

# stripe.api_key = settings.STRIPE_SECRET


@login_required
def charity(request):
    """CHARITIES PAGE"""
    charities = Charity.objects.all()
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    donations = DonationLineItem.objects.all()
    # Adding 1235 for display purposes ;)
    donation_count = len(donations) * 5 + 1235
    charity_count = len(charities)

    context = {"charities": charities, "my_profile": my_profile, 'donation_count': donation_count,
               'charity_count': charity_count}

    return render(request, "charity.html", context)


@login_required
def propose_charity(request):
    """ADMIN ADDS NEW CHARITY"""
    if not request.user.is_superuser:
        raise Http404

    if request.method == 'POST':

        form = ProposeCharityForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            donation = 5  ## fixed 5eu donation amount
            image = form.cleaned_data['image']

            new_charity = Charity.objects.create(
                name=name,
                description=description,
                donation=donation,
                image=image,
            )
            new_charity.save()

            return redirect(reverse('charity:charity'))


    else:
        form = ProposeCharityForm()

    return render(request, 'propose_charity.html', {'form': form})


def delete_charity(request, pk):
    """ADMIN'S DELETE CHARITY"""
    if not request.user.is_superuser:
        raise Http404

    if request.method == 'DELETE':
        charity = get_object_or_404(Charity, pk=pk)
        charity.delete()

        return redirect(reverse('charity:charity'))


def view_donations(request):
    """VIEW CHOSEN DONATIONS"""
    return render(request, "view_donations.html")


def add_to_donations(request, id):
    """CHOSE YOUR DONATION"""
    quantity = 1  ## fixed quantity allowed per one session

    chosen_donations = request.session.get('chosen_donations', {})
    chosen_donations[id] = chosen_donations.get(id, quantity)

    request.session['chosen_donations'] = chosen_donations
    return redirect(reverse('charity:charity'))


def adjust_donations(request, id):
    """CHOOSE YOUR DONATION"""
    chosen_donations = request.session.get('chosen_donations', {})

    chosen_donations.pop(id)

    request.session['chosen_donations'] = chosen_donations
    return render(request, "view_donations.html")


@login_required()
def charity_donation(request):

    if request.method == "POST":
        donation_form = DonationForm(request.POST)
        make_donation_form = MakeDonationForm(request.POST)

        messages.success(request, "Your Donation was successful. Thank you!")
        return redirect(reverse('charity:charity'))

        ### PAYMENT
        # if donation_form.is_valid() and make_donation_form.is_valid():
        #     donation = donation_form.save(commit=False)
        #     donation.save()
        #
        #     chosen_donations = request.session.get('chosen_donations',
        #                                            {})  # request context from charity_choice app
        #     total = 0
        #     for id, quantity in chosen_donations.items():
        #         charity = get_object_or_404(Charity, pk=id)
        #         total += quantity * charity.donation
        #         donation_line_item = DonationLineItem(
        #             donation=donation,
        #             charity=charity
        #         )
        #         donation_line_item.save()


        #     try:
        #         customer = stripe.Charge.create(
        #             amount=int(total * 100),  ## counts in cents
        #             currency="EUR",
        #             description=request.user.email,
        #             card=make_donation_form.cleaned_data['stripe_id'],
        #         )
        #     except stripe.error.CardError:
        #         messages.error(request, "Your card was declined!")
        #
        #     if customer.paid:
        #         messages.error(request, "You have successfully paid")
        #         request.session['chosen_donations'] = {}
        #         return redirect(reverse('charity:charity'))
        #     else:
        #         messages.error(request, "Unable to take payment")
        # else:
        #     print(make_donation_form.errors)
        #     messages.error(request, "We were unable to take a payment with that card!")



    else:
        donation_form = DonationForm()
        make_donation_form = MakeDonationForm()

    return render(request, "charity_donation.html", {'donation_form': donation_form,
                                                     'make_donation_form': make_donation_form,
                                                     })
