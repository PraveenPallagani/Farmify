from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signUp(request:HttpRequest):
    return HttpResponse("SignUp Page")

def signIn(request:HttpRequest):
    # rediret to home if aleady authenticated
    if request.user and request.user.is_authenticated:
        return redirect("Home")
    # authenticate and login the user
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        # handle signIn validations
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have logged in successfully!")
            return redirect("Home")
        else:
            messages.error(request, "Invalid phone number or password.")
    # serve the login page
    return render(request=request,template_name='login.html')

