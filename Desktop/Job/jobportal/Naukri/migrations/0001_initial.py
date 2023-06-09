# Generated by Django 4.2 on 2023-04-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="login",
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
                ("email", models.EmailField(max_length=50, null=True)),
                ("password", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="signup",
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
                ("name", models.CharField(max_length=50, null=True)),
                ("email", models.EmailField(max_length=50, null=True)),
                ("password", models.CharField(max_length=50, null=True)),
                ("mobile", models.IntegerField(max_length=10, null=True)),
                ("otp", models.IntegerField(max_length=4, null=True)),
            ],
        ),
    ]
