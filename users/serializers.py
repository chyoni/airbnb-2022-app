from . import models
from rest_framework import serializers


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "superhost",
        ]


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = [
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        ]
