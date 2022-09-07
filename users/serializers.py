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
            "bio",
            "address",
            "job",
            "avatar",
            "superhost",
            "date_joined",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "bio",
            "address",
            "job",
            "superhost",
            "password",
            "date_joined",
        ]
        read_only_fields = ["id", "superhost", "avatar"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = models.User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
