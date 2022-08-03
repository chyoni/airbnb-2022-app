from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rooms.serializers import RoomSerializer
from . import models


class ListRoomsView(ListAPIView):

    queryset = models.Room.objects.all()
    serializer_class = RoomSerializer
