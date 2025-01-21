from rest_framework import serializers
from .models import Profile, User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "father_name",
            "birthday_date",
            "gender",
            "phone_number",
            "user_type",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "avatar"]
