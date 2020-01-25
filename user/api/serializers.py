from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _  # future translations

from rest_framework import serializers
from core.models import MyProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    # making sure that the password is set with "set_password" function
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        # remove password
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)  # Call ModelSerializer default update function

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False  # include whitespace in password if any
    )

    # overwrite django validate function
    def validate(self, attrs):
        """Validate and  authenticate the  user"""
        email = attrs.get('email')
        password = attrs.get('password')

        # django-provided auth function
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            message = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(message, code='authentication')

        attrs['user'] = user
        return attrs  # overwritten validate function must return attrs

class MyProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile"""

    class Meta:
        model = MyProfile
        fields = '__all__'
        read_only_fields = ('id','my_wallet')

