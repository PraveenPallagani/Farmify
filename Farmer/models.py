from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Category(models.Model):
    CATEGORIES = [
        ('vegetables','Vegetables'),
        ('fruits','Fruits')
    ]
    name = models.CharField(max_length=50,choices=CATEGORIES,unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    UNITS = [
        ('kilograms', 'kgs'),
        ('liters', 'ltrs')
    ]
    # user foreign key
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    # product fields
    name = models.CharField(max_length=100)
    description = models.TextField()
    measure_unit = models.CharField(max_length=10,choices=UNITS)
    quantity = models.PositiveIntegerField()
    discounted_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.price}/{self.measure_unit}'
    
    def save(self,*args, **kwargs):
        if not self.user or self.user.role != 'farmer':
            raise ValidationError("The user must be a farmer to create a product.")
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at'] 


def upload_by_user(instance, filename):
    return f'{instance.product.user.phone_number}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_by_user)   

    def __str__(self):
        return f'Image {self.image} for {self.product.name}'