from django.contrib import admin
from core import views
from django.urls import path,include

admin.site.site_header = "GoGlide Admin"
admin.site.site_title = "GoGlide Admin Portal"
admin.site.index_title = "Welcome to GoGlide Portal"


urlpatterns = [
    path('',views.index,name='home'),
    path('admin/',admin.site.urls),
   

]