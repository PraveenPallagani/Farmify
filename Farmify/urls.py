
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views as main_view
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view.home,name="Home"),
    path('auth/',include('Authentication.urls')),
    path('customer/',include('Customer.urls')),
    path('farmer/',include('Farmer.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'Farmify.views.handle_404'