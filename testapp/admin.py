from django.contrib import admin
from testapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','name','category','price','manufacture_date','expiry_date')

admin.site.register(Product, ProductAdmin)

