# Generated by Django 5.0.2 on 2024-04-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PicStock",
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
                ("owner", models.CharField(max_length=150)),
                ("name", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="picstock/")),
                ("uploaded_datetime", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["uploaded_datetime"],
            },
        ),
    ]
