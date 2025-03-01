from django.contrib import messages
from .models import Product, Category, ProductImage
from django.http import *
from django.shortcuts import *
from django.core.files.storage import default_storage
import os

options = {'Home': '/farmer/home', 'All products': '/farmer/all-products', 'Add new product': '/farmer/add-product'}


def add_product(request:HttpRequest):
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
    return redirect('All Products')


def update_product(request: HttpRequest, product_id:int):
    if request.POST.get('_method') == 'DELETE_IMAGE':
        delete_image(request)
    elif request.POST.get('_method') == 'UPDATE':
        pass
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product, 'options': options}
    return render(request, 'farmer/add-product.html', context)

def delete_product(product:Product):
    # delete images of the product
    images = product.images.all()
    for img in images:
        if os.path.isfile(img.image.path):
            os.remove(img.image.path)
    # then delete the product
    product.delete()
    messages.info(request, f'Product {product.name} is deleted successfully by {request.user}')
    return redirect('All Products')

def delete_image(request: HttpRequest):
    image_id = request.POST.get('_image')
    image = get_object_or_404(ProductImage, id=image_id)
    default_storage.delete(image.image.path)
    image.delete()


def validateImagesCount(request:HttpRequest, images:list):
    if len(images)==0:
        messages.error(request, 'Atleast one image of product should be upload')
        return False
    if len(images)>5:
        messages.error(request, 'At max only 5 images of product can be upload')
        return False
    return True
