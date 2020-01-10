from rest_framework import serializers
from core.models_charity import Charity, Donation, DonationLineItem


class CharitySerializer(serializers.ModelSerializer):
    """Serializer for new charity event"""

    class Meta:
        model = Charity
        fields = '__all__'
        read_only_fields = ('id', 'donation')

class DonationSerializer(serializers.ModelSerializer):
    """Donation checkout serializer"""

