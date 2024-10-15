
from django.urls import path
from . import views as auth_view
   

urlpatterns = [
    path('signup', auth_view.signUp),
    path('signin', auth_view.signIn),
]