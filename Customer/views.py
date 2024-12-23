from django.shortcuts import render
from django.http import *
from Authentication.decorators import role_required

@role_required('customer')
def home(request:HttpRequest):
    return render(request, 'customer/home.html')
