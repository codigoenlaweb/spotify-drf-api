# Generated by Django 4.1.2 on 2022-10-26 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("album", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="duration",
            field=models.DurationField(
                blank=True, default=datetime.timedelta(0), verbose_name="duration"
            ),
        ),
    ]
