from PIL import Image
from io import BytesIO
from pyexpat import model
from itertools import product
from django.contrib import admin
from django.core.files import File
from .models import Category, Product, ProductImage, ProductVarient


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    exclude = ('slug',)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5
    min_num = 1


class ProductVarientAdmin(admin.TabularInline):
    model = ProductVarient
    extra = 1
    max_num = 5
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageAdmin,
        ProductVarientAdmin,
    ]
    list_display = ('title', 'category', 'price', 'date_added')
    list_display_links = ('title', )
    list_filter = ('category', )
    exclude = ('slug',)

    class Meta:
        model = Product


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product,ProductAdmin)
# admin.site.register(ProductImage)
