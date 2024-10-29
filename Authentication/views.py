from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def signUp(request:HttpRequest):
    # rediret to home if aleady authenticated
    if request.user and request.user.is_authenticated and request.user.role in ('farmer', 'customer'):
        return redirect('Home')
    # create the user and redirect to login page
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        password = request.POST.get('password') 
        try:
            user = CustomUser.objects.create_user(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                role=role,
                password=password
            )
            user.save()
            messages.success(request, 'User created successfully!!')
            return redirect('SignIn')
        except Exception as ex:
            messages.error(request, f'Exception while saving the user: {ex}')

    # serve the signup page
    return render(request=request, template_name='authentication/signup.html')



def signIn(request:HttpRequest):
    # rediret to home if aleady authenticated
    if request.user and request.user.is_authenticated and request.user.role in ('farmer', 'customer'):
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
    # serve the signin page
    return render(request=request,template_name='authentication/signin.html')


def signOut(request):
    logout(request)
    messages.success(request, 'Successfully signed out!!')
    return redirect('SignIn')

