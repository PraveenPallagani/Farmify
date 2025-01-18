from django.shortcuts import render, redirect
from django.http import *
from Authentication.decorators import role_required
from django.contrib import messages
from .models import Product, Category, ProductImage

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
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_measure_unit = request.POST.get('product_measure_unit')
        product_category = request.POST.get('product_category')
        product_quantity = request.POST.get('product_quantity')
        product_price = request.POST.get('product_price')
        images = request.FILES.getlist('images')
        # validate no of images 
        if not validateImagesCount(request,images):
            return redirect("Add Product")
        # get the category instance
        category = Category.objects.get(name = product_category)
        # create the prodct object and save
        product = Product.objects.create(user=request.user,category=category,name=product_name,description=product_desc,
            measure_unit=product_measure_unit,quantity=product_quantity,price=product_price)
        product.save()
        # now create the images
        for image in images:
            product_image = ProductImage.objects.create(product=product, image=image)
            product_image.save()
        # add the success message
        messages.success(request, f"{product} is created successfully by {request.user}")
    # serve the add product form
    return render(request,'farmer/add-product.html', context)


@role_required('farmer')
def all_products(request):
    products = Product.objects.all()
    context = {'options':options, 'products':products}
    print(products)
    return render(request,'farmer/all-products.html',context)

@role_required('farmer')
def product_details(request,id):
    product = Product.objects.get(id=id)
    context = {'options':options, 'product':product}
    return render(request, 'farmer/product-details.html',context)


def validateImagesCount(request:HttpRequest, images:list):
    if len(images)==0:
        messages.error(request, 'Atleast one image of product should be upload')
        return False
    if len(images)>5:
        messages.error(request, 'At max only 5 images of product can be upload')
        return False
    return True
