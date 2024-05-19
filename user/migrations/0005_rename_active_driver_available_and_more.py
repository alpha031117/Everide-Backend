# Generated by Django 5.0 on 2024-05-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_myuser_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="driver",
            old_name="active",
            new_name="available",
        ),
        migrations.AddField(
            model_name="driver",
            name="current_latitude",
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name="driver",
            name="current_longtidue",
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
    ]
