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



]