import stripe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from rest_framework import viewsets, status, filters, views
from rest_framework.response import Response

from charity import serializers
from core.models_charity import Charity, DonationLineItem
from core.permissions import IsAdminOrReadOnly
from .forms import DonationForm, MakeDonationForm


# stripe.api_key = settings.STRIPE_SECRET


@login_required()
def charity_donation(request):
    if request.method == "POST":
        donation_form = DonationForm(request.POST)
        make_donation_form = MakeDonationForm(request.POST)

        messages.success(request, "Your Donation was successful. Thank you!")
        return redirect(reverse('charity:charity'))

        # ## PAYMENT
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
        #
        #
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


class CharityViewSet(viewsets.ModelViewSet):
    """Charity events viewset"""
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = serializers.CharitySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)
    ordering_fields = '__all__'
    queryset = Charity.objects.all()

    def get_queryset(self):
        """Return list of charities"""
        queryset = self.queryset
        return queryset.order_by('name')

    def retrieve(self, request, pk=None):
        """Retrieve charity details"""
        queryset = Charity.objects.all()
        charity_instance = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CharitySerializer(charity_instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Delete charity"""
        try:
            queryset = Charity.objects.all()
            charity_instance = get_object_or_404(queryset, pk=pk)
            self.perform_destroy(charity_instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonateView(views.APIView):

    def get(self, request):
        return Response({"message": "Please visit our Fundraising Actions and become a part of our charity program."})

    def post(self):
        data = request.data
        return Response({'data': data})

