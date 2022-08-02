from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rooms.serializers import RoomSerializer
from . import models


@api_view(["GET"])
def list_rooms(request):
    rooms = models.Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)
