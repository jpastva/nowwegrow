''' Admin modules for shop app '''
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ''' Allow slug field to prepopulate from category name '''
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ''' Allow product slug to prepoluate from name '''
    list_display = ['name', 'slug', 'unit_price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['unit_price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    