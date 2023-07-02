# Generated by Django 4.2.2 on 2023-07-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_customer_user_alter_driver_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="drop_off_loc",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="pick_up_loc",
        ),
        migrations.AlterField(
            model_name="customer",
            name="gender",
            field=models.CharField(default="none", max_length=10),
        ),
        migrations.AlterField(
            model_name="driver",
            name="gender",
            field=models.CharField(default="none", max_length=10),
        ),
    ]
