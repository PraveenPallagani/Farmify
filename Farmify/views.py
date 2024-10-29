from django.shortcuts import render,redirect
from django.http import *
from Authentication.decorators import role_required

@role_required('customer','farmer')
def home(request:HttpRequest):
    if request.user.role =='farmer':
        return redirect('Farmer Home')
    elif request.user.role == 'customer':
        return redirect('Customer Home')
    else:
        return HttpResponse("This is not expected from the home route")