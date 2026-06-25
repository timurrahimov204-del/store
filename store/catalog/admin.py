from catalog.models import Category, Product
from django.contrib import admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'date_created_at', 'date_updated_at']
    list_editable = ['price']
    list_filter = ['date_created_at', 'date_updated_at']
