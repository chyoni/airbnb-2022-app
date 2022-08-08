from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from . import models


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = models.Room
        exclude = ["modified"]
        read_only_fields = ["user", "id", "created", "updated"]

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

    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False
