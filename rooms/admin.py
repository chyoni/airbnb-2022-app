from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "photo_number",
    )

    ordering = ["-created"]


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
