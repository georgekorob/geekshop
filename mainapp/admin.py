from django.contrib import admin

# Register your models here.
from authapp.models import UserProfile
from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(UserProfile)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('name', 'price',)
    search_fields = ('name',)
