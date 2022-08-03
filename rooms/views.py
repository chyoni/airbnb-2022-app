from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rooms.serializers import RoomSerializer, BigRoomSerializer
from . import models


class ListRoomsView(ListAPIView):

    queryset = models.Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):

    queryset = models.Room.objects.all()
    serializer_class = BigRoomSerializer
