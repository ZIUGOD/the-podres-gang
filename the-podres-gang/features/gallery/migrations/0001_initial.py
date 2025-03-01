# Generated by Django 5.1.6 on 2025-02-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="gallery/images/")),
                ("caption", models.CharField(max_length=128)),
                (
                    "pub_date",
                    models.DateField(auto_now_add=True, verbose_name="Uploaded at "),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=512, null=True),
                ),
            ],
        ),
    ]
