from django.shortcuts import redirect
from django.http import *
from Authentication.decorators import role_required
from django.contrib import messages

@role_required('customer','farmer')
def home(request:HttpRequest):
    if request.user.role =='farmer':
        return redirect('Farmer Home')
    elif request.user.role == 'customer':
        return redirect('Customer Home')
    else:
        return HttpResponse("This is not expected from the home route")

@role_required('customer','farmer')  
def handle_404(request,exception):
    messages.error(request, f'Requested url "{request.get_full_path()}" is invalid')
    return redirect("Home")