from rest_framework import serializers
from users.serializers import TinyUserSerializer
from . import models


class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = models.Room
        fields = ["name", "price", "instant_book", "user"]
