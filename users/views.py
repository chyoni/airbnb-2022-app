from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rooms import models as room_models
from rooms.serializers import RoomSerializer
from . import models
from .serializers import ReadUserSerializer, WriteUserSerializer


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            data=ReadUserSerializer(request.user).data, status=status.HTTP_200_OK
        )

    def put(self, request):
        serializer = WriteUserSerializer(request.user, request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                data=ReadUserSerializer(user).data, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = models.User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data, status=status.HTTP_200_OK)
    except models.User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class FavsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = RoomSerializer(user.favs.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        pk = request.data.get("pk", None)
        user = request.user
        if pk is not None:
            try:
                room = room_models.Room.objects.get(pk=pk)
                if room in user.favs.all():
                    user.favs.remove(room)
                else:
                    user.favs.add(room)
                return Response(status=status.HTTP_200_OK)
            except room_models.Room.DoesNotExist:
                return Response(
                    data=f"Room does not exist with the pk: {pk}",
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                data="Room pk required.", status=status.HTTP_400_BAD_REQUEST
            )
