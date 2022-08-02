from django.core import serializers
from django.http import HttpResponse
from rooms import models as room_models


def list_rooms(request):
    data = serializers.serialize(format="json", queryset=room_models.Room.objects.all())
    response = HttpResponse(content=data)
    return response
