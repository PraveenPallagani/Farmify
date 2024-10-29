from django.shortcuts import render
from django.http import *
from Authentication.decorators import role_required
from django.contrib import messages
from .models import Product

@role_required('farmer')
def farmer_home(request:HttpRequest):
    return render(request,'farmer/home.html')


@role_required('farmer')
def add_product(request):
    # handle the form data and create the product
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_measure_unit = request.POST.get('product_measure_unit')
        product_quantity = request.POST.get('product_quantity')
        product_price = request.POST.get('product_price')
        # create the prodct object and save
        product = Product.objects.create(user=request.user,name=product_name,description=product_desc,
            measure_unit=product_measure_unit,quantity=product_quantity,price=product_price)
        product.save()
        # add the success message
        messages.success(request, f"{product} is created successfully by {request.user}")
    # serve the add product form
    return render(request,'farmer/add-product.html')


@role_required('farmer')
def all_products(request):
    products = Product.objects.all()
    context = {'products':products}
    print(products)
    return render(request,'farmer/all-products.html',context)

@role_required('farmer')
def product_details(request,id):
    product = Product.objects.get(id=id)
    context ={'product':product}
    return render(request, 'farmer/product-details.html',context)