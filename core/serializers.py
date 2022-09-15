from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

