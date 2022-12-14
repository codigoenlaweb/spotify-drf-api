# Generated by Django 4.1.2 on 2022-10-26 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("album", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Track",
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
                ("title", models.CharField(max_length=250, verbose_name="title")),
                (
                    "duration",
                    models.DurationField(
                        blank=True, default=0, verbose_name="duration"
                    ),
                ),
                (
                    "url_track",
                    models.URLField(max_length=250, verbose_name="url track"),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tracks",
                        related_query_name="track",
                        to="album.album",
                        verbose_name="artist",
                    ),
                ),
            ],
            options={
                "verbose_name": "Track",
                "verbose_name_plural": "Tracks",
            },
        ),
    ]
