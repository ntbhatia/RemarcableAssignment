from django.contrib import admin
from .models import Category, Tag, Product

admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'tags']
    search_fields = ['name']
