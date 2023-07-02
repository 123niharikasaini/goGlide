from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime

User=get_user_model() # get the model of current logged in use

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    # pick_up_loc = models.CharField(max_length=200)
    # drop_off_loc = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    email_id = models.EmailField(max_length=100)
    # postcode = models.IntegerField()
    address = models.CharField(max_length=200)
    gender=models.CharField(max_length=10,default="none")

    class Meta:
        # meta data
        # telling django to sort the data on column 
        ordering=['-date']

    def __str__(self):
        return self.name


class Driver(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=False)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    licence_no = models.IntegerField()
    vehicle_no = models.IntegerField()
    vehicle_type = models.CharField(max_length=200)
    D_O_B = models.DateField(max_length=200)
    gender=models.CharField(max_length=10,default="none")
    date = models.DateTimeField(default=datetime.now)


    class Meta:
        # meta data
        # telling django to sort the data on column 
        ordering=['-date']

    def __str__(self):
        return self.name