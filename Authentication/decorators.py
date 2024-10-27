from django.shortcuts import redirect
from functools import wraps
from django.http import HttpRequest
from django.contrib import messages

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request:HttpRequest, *args, **kwargs):
            if not request.user or not request.user.is_authenticated:
                messages.error(request, "Please login to access the requested route!!")
                return redirect('SignIn')  # Redirect to login page
            
            if request.user.role not in roles:
                messages.error(request, f"Only user with {roles} roles can access the '{request.get_full_path()}'")
                return redirect('Home')  # Redirect to a home page
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
