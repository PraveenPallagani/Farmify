from django.http import *
from Authentication.decorators import role_required

@role_required('customer','farmer','admin')
def home(request:HttpRequest):
    return HttpResponse(f"This is home page by {request.user}")