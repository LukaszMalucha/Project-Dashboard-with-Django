from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters, authentication, permissions, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from charity import serializers
from core.models import MyProfile
from core.models_charity import CharityModel, DonationModel
from core.permissions import IsAdminOrReadOnly


class CharityViewSet(viewsets.ModelViewSet):
    """Charity events viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    serializer_class = serializers.CharityModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)
    ordering_fields = '__all__'
    queryset = CharityModel.objects.all()

    def get_queryset(self):
        """Return list of charities"""
        queryset = self.queryset
        return queryset.order_by('name')

    def retrieve(self, request, pk=None, **kwargs):
        """Retrieve charity details"""
        queryset = CharityModel.objects.all()
        charity_instance = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CharityModelSerializer(charity_instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None, **kwargs):
        """Deleting charity event"""
        queryset = CharityModel.objects.all()
        charity_instance = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(charity_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonateView(views.APIView):
    """Donation viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response({"message": "Please visit our Fundraising Actions and become a part of our charity program."},
                        status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data['checkout']
        total = len(data) * 5
        queryset = CharityModel.objects.all()
        my_profile = get_object_or_404(MyProfile, owner=request.user)
        if my_profile.my_wallet < total:
            return Response({"error": "Insufficient leancoins to proceed with the transaction."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            for element in data:
                charity = get_object_or_404(queryset, pk=int(element))
                DonationModel.objects.create(donor=request.user, charity=charity)
            my_profile.my_wallet -= total
            my_profile.save()
        except Http404:
            return Response({"error": "We couldn't proceed with transaction at this time. Try again later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": "You have successfully paid"}, status=status.HTTP_201_CREATED)
