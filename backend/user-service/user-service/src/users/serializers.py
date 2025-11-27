from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'preferences',
            'is_active',
            'date_joined',
            'updated_at',
        ]


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'preferences']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'profile_picture']
