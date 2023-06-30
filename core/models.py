from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.IntegerField(max_length=200)
    pick_up_loc = models.CharField(max_length=200)
    drop_off_loc = models.CharField(max_length=200)
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)
    email_id = models.EmailField(max_length=100)
    postcode = models.IntegerField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.IntegerField(max_length=200)
    email_id = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=False)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    licence_no = models.IntegerField(max_length=200)
    vehicle_no = models.IntegerField(max_length=200)
    vehicle_type = models.CharField(max_length=200)
    D_O_B = models.DateField(max_length=200)

    def __str__(self):
        return self.name

