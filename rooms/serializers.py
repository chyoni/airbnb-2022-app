from rest_framework import serializers
from users.serializers import UserSerializer
from . import models


class ReadRoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Room
        exclude = ["modified"]


class WriteRoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    beds = serializers.IntegerField()
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    class Meta:
        model = models.Room
        fields = [
            "name",
            "address",
            "price",
            "beds",
            "lat",
            "lng",
            "bedrooms",
            "bathrooms",
            "check_in",
            "check_out",
            "instant_book",
        ]

    def create(self, validated_data):
        return models.Room.objects.create(**validated_data)

    def validate(self, data):
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError(
                "Check out time must bigger then check in time"
            )
        return data
