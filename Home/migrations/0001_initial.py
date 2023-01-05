# Generated by Django 4.1.4 on 2022-12-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=30)),
                ("phone", models.BigIntegerField()),
                ("comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Posts",
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
                ("title", models.CharField(max_length=150)),
                ("discription", models.TextField()),
                ("web_site", models.CharField(blank=True, max_length=250)),
                ("date_time", models.DateTimeField(auto_now=True)),
                ("modification", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(blank=True, upload_to="media/pictures")),
            ],
        ),
    ]