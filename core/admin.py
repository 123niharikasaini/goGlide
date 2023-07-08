from django.contrib import admin
from .models import Customer
from .models import Driver,Booking,Rent_info

# Register your models here.
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Booking)
admin.site.register(Rent_info)