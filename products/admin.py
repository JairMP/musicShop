from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'brand', 'description', 'price', 'stock', 'image')
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(Product, ProductAdmin)


