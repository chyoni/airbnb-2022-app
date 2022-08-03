from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [path("", views.ListRoomsView.as_view(), name="rooms")]
