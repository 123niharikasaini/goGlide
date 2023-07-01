# Generated by Django 4.1.7 on 2023-06-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("contact_no", models.IntegerField(max_length=200)),
                ("pick_up_loc", models.CharField(max_length=200)),
                ("drop_off_loc", models.CharField(max_length=200)),
                ("date", models.DateField(max_length=150)),
                ("time", models.TimeField(max_length=150)),
                ("email_id", models.EmailField(max_length=100)),
                ("postcode", models.IntegerField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("contact_no", models.IntegerField(max_length=200)),
                ("email_id", models.EmailField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
                ("gender", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("licence_no", models.IntegerField(max_length=200)),
                ("vehicle_no", models.IntegerField(max_length=200)),
                ("vehicle_type", models.CharField(max_length=200)),
                ("D_O_B", models.IntegerField(max_length=200)),
            ],
        ),
    ]
