# Generated by Django 5.1.6 on 2025-02-17 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="caption",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=24)),
                ("password", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=64)),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("date_joined", models.DateField(auto_now_add=True)),
                ("last_login", models.DateField(auto_now=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "images",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gallery.image",
                    ),
                ),
            ],
        ),
    ]
