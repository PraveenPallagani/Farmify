
from django.urls import path
from . import views as auth_view
   

urlpatterns = [
    path('signup', auth_view.signUp,name='SignUp'),
    path('signin', auth_view.signIn,name='SignIn'),
    path('signout', auth_view.signOut,name='SignOut'),
]