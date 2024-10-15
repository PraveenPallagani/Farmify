from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class CustomUserAdmin(BaseUserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    ordering = ('phone_number', )

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ("Personal Info", {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request,obj,kwargs)
        return form
    
    search_fields= ('phone_number', 'first_name', 'last_name')
    filter_horizontal = ()
    list_editable = ('is_active','is_staff')

# Register your models here.
admin.site.register(models.CustomUser,CustomUserAdmin)
