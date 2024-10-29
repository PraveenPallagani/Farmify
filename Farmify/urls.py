
from django.contrib import admin
from django.urls import path,include
from . import views as main_view
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view.home,name="Home"),
    path('auth/',include('Authentication.urls')),
    path('customer/',include('Customer.urls')),
    path('farmer/',include('Farmer.urls'))
]

handler404 = 'Farmify.views.handle_404'