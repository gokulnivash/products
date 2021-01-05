from django.contrib import admin

# Register your models here.
from product.models import LoginRole, Product


class UserroleAdmin(admin.ModelAdmin):
    list_display = ['id','user','role_type','access_type','created_by','modified_by']
admin.site.register(LoginRole,UserroleAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','is_active','created_by','modified_by']
admin.site.register(Product,ProductAdmin)

