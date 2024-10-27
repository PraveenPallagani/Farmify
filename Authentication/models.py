from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, role='admin', **extra_fields):
        # validations
        if not phone_number:
            raise ValueError("Phone number is required")
        if password and len(password) < 4:
            raise ValueError('Password should contain atleast 4 charecters')
        # save the user to db
        extra_fields.setdefault('role',role)
        user = self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(phone_number=phone_number,password=password, role='admin', **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # roles
    ADMIN = 'admin'
    FARMER = 'farmer'
    CUSTOMER = 'customer'
    ROLES = [
        (ADMIN,'Admin'),
        (FARMER,'Farmer'),
        (CUSTOMER,'Customer')
    ]
    # user properties
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # user roles
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10,choices=ROLES, default=ADMIN)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']
    
    def __str__(self):
        return f'{self.first_name} - {self.phone_number}'
