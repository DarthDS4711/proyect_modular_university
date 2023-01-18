from django.contrib import admin

from core.product.models import Category, Product, Size

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
