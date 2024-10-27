from django.http import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request:HttpRequest):
    return HttpResponse(f"This is home page by {request.user}")