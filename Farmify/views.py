from django.http import *

def home(request:HttpRequest):
    return HttpResponse("This is home page")