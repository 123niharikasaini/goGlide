from django.contrib import admin
from core import views
from django.urls import path




urlpatterns = [
    path('',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('signOut',views.signOut,name="signOut"),
    path('signup',views.signup,name="signup"),
    path('midConfirm',views.mid,name="midConfirm"),
    path('driverdetails',views.driverdetails,name="driverdetails"),
    path('submit',views.submit,name="submit"),
    path('book',views.book,name="book"),
    path('rent',views.rent,name="rent"),
    path('driverLogin',views.driverLogin,name="driverLogin"),

]