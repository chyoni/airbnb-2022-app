from . import models
from rest_framework import serializers


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["pk", "username", "superhost"]
