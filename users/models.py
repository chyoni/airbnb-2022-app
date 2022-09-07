from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("rooms.Room", related_name="favs", blank=True)
    bio = models.CharField(blank=True, max_length=200)
    address = models.CharField(blank=True, max_length=300)
    job = models.CharField(blank=True, max_length=150)

    def room_count(self):
        return self.rooms.count()

    room_count.short_description = "Room Count"
