from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "superhost", "favs", "bio", "job", "address")},
        ),
    )

    list_display = UserAdmin.list_display + (
        "id",
        "room_count",
    )
