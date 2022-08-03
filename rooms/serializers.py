from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from . import models


class ReadRoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = models.Room
        exclude = ["modified"]


class WriteRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        exclude = ["user", "modified", "created"]

    def create(self, validated_data):
        return models.Room.objects.create(**validated_data)

    def validate(self, data):
        if not self.instance:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
            if check_in == check_out or check_in > check_out:
                raise serializers.ValidationError(
                    "Check out time must bigger then check in time"
                )
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out", self.instance.check_out)
            if check_in is not None:
                if check_in == check_out or check_in > check_out:
                    raise serializers.ValidationError(
                        "Check out time must bigger then check in time"
                    )
        return data
