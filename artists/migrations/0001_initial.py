# Generated by Django 4.2.11 on 2024-05-28 19:48

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("year", models.IntegerField()),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="artists.artist"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="album",
            constraint=models.UniqueConstraint(
                fields=("artist", "name", "year"), name="artist_album_year"
            ),
        ),
    ]
