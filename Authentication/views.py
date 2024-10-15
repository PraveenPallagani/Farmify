from django.shortcuts import render
from django.http import *

# Create your views here.
def signUp(request:HttpRequest):
    return HttpResponse("SignUp Page")

def signIn(request:HttpRequest):
    return HttpResponse("SignIn Page")

