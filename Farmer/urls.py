from django.urls import path
from . import views as farmer_view

urlpatterns = [
    path('home',farmer_view.home,name="Home")
]
