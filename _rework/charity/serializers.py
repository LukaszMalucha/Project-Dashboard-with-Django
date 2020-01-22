from rest_framework import serializers
from core.models_charity import CharityModel, DonationModel


class CharityModelSerializer(serializers.ModelSerializer):
    """Serializer for new charity event"""

    class Meta:
        model = CharityModel
        fields = '__all__'
        read_only_fields = ('id', 'donation')