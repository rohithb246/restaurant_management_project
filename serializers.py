from django.contrib.auth.models import User
from rest_framework import serializers

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['first_name', 'last_name', 'email']
        extra_kwargs = {
            'email': {'required': False},
        }