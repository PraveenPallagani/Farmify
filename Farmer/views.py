from django.shortcuts import render
from django.http import *
from Authentication.decorators import role_required

@role_required('farmer')
def home(request:HttpRequest):
    return HttpResponse("Farmer Home Page")

@role_required('farmer')
def add_product(request):
    return HttpResponse("Add Product Page")

@role_required('farmer')
def all_products(request):
    return HttpResponse("See All Of Your Products")

@role_required('farmer')
def product_details(request):
    return HttpResponse("Product Details Page")