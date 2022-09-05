# Generated by Django 4.1 on 2022-09-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_alter_room_lat_alter_room_lng"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="lat",
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
        migrations.AlterField(
            model_name="room",
            name="lng",
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
