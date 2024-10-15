from django.urls import path
from .import views as customer_view

urlpatterns = [
    path('home',customer_view.home,name="Home")
]
