# Generated by Django 4.1 on 2022-09-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0005_alter_room_lat_alter_room_lng"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="lat",
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name="room",
            name="lng",
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
