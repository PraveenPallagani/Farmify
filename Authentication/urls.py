
from django.urls import path
from . import views as auth_view
   

urlpatterns = [
    path('signup', auth_view.signUp,name='signUp'),
    path('signin', auth_view.signIn,name='signIn'),
]