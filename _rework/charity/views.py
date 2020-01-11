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

    def post(self, request):
        data = request.data['checkout']
        for element in data:
            pass

        return Response({'data': data})

