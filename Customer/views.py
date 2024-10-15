from django.shortcuts import render
from django.http import *

# Create your views here.
def home(request:HttpRequest):
    return HttpResponse('Customer Home Page')
