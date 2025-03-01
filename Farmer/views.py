from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from Authentication.decorators import role_required
from django.contrib import messages
from .models import Product, Category, ProductImage
from . import view_helper
import os

options = {'Home': '/farmer/home', 'All products': '/farmer/all-products', 'Add new product': '/farmer/add-product'}

@role_required('farmer')
def farmer_home(request:HttpRequest):
    context = {'options':options}
    return render(request,'farmer/home.html', context)


@role_required('farmer')
def add_product(request):
    context = {'options':options}
    # handle the form data and create the product
    if request.method == 'POST':
        return view_helper.add_product(request)
    # serve the add product form
    return render(request,'farmer/add-product.html', context)

@role_required('farmer')
def update_product(request,id):
    print(f'product id to update {id}')
    # handle the form data and create the product
    if request.method == 'POST':
        return view_helper.update_product(request, id)
    # serve the add product form
    return redirect('All Products')


@role_required('farmer')
def all_products(request):
    products = Product.objects.all()
    context = {'options':options, 'products':products}
    print(products)
    return render(request,'farmer/all-products.html',context)

@role_required('farmer')
def product_details(request:HttpRequest,id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        print(f'Deletign the product: {product.id}')
        return view_helper.delete_product(product)

    context = {'options':options, 'product':product}
    return render(request, 'farmer/product-details.html',context)


