from django.contrib import admin

from product.models import Product,categorie
# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name', 'price']


# Register your models here.
# admin.site.register(Product, AdminProduct)
admin.site.register(Product)
admin.site.register(categorie)