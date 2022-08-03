from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rooms import serializers
from rooms.serializers import ReadRoomSerializer, WriteRoomSerializer
from . import models


# @api_view(["GET", "POST"])
# def rooms_view(request):
#     if request.method == "GET":
#         rooms = models.Room.objects.all()
#         serializer = ReadRoomSerializer(rooms, many=True).data
#         return Response(serializer)
#     elif request.method == "POST":
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         serializer = WriteRoomSerializer(data=request.data)
#         if serializer.is_valid():
#             room = serializer.save(user=request.user)
#             room_serializer = ReadRoomSerializer(room).data
#             return Response(status=status.HTTP_200_OK, data=room_serializer)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomsView(APIView):
    def get(self, request):
        rooms = models.Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            return Response(status=status.HTTP_200_OK, data=room_serializer)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    def get(self, request, pk):
        try:
            room = models.Room.objects.get(pk=pk)
            serializer = ReadRoomSerializer(room).data
            return Response(status=status.HTTP_200_OK, data=serializer)
        except models.Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        pass

    def delete(self, request):
        pass
