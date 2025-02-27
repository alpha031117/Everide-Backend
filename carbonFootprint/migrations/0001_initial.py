# Generated by Django 5.0 on 2024-05-13 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarbonFootprint",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("footprint", models.FloatField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carbon_footprint",
                        to="user.myuser",
                    ),
                ),
            ],
        ),
    ]
