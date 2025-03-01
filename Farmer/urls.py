from django.urls import path
from . import views as farmer_view

urlpatterns = [
    path('home',farmer_view.farmer_home,name="Farmer Home"),
    path('add-product',farmer_view.add_product,name="Add Product"),
    path('update-product/<int:id>',farmer_view.update_product,name="Update Product"),
    path('all-products',farmer_view.all_products,name="All Products"),
    path('product-details/<int:id>',farmer_view.product_details,name="Prodyuct Details")
]
