
from django.contrib import admin
from django.urls import path
from . import views as main_view
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view.home,name="Home")
]