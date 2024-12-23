from django.shortcuts import render
from django.http import *
from django.db.models import Q
from Authentication.decorators import role_required
from Farmer.models import Product, Category

@role_required('customer')
def home(request:HttpRequest):
    products = None
    search_query = None
    categories = Category.objects.all()
    if request.method == 'POST':
        search_query = request.POST.get('search')
    else:
        search_query = request.GET.get('category')
    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query) | 
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'customer/home.html', context)
