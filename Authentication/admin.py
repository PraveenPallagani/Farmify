from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class CustomUserAdmin(BaseUserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff','role')
    ordering = ('phone_number', )

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ("Personal Info", {'fields': ('first_name', 'last_name','role')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'first_name', 'last_name', 'role')}
        ),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request,obj,**kwargs)
        return form
    
    search_fields= ('phone_number', 'first_name', 'last_name')

# Register your models here.
admin.site.register(models.CustomUser,CustomUserAdmin)
