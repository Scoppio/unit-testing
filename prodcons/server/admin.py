from django.contrib import admin
from .models import Company, Product, ProductEntry


admin.site.register(Company)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'msrp', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('name', 'id')
    ordering = ('name', 'msrp', 'created_at', 'updated_at', 'deleted_at')


class ProductEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'company', 'quantity', 'price_per_unit', 'date', 'created_at', 'updated_at')
    list_filter = ('product', 'company', 'date', 'created_at', 'updated_at')
    search_fields = ('product', 'company')
    ordering = ('product', 'company', 'quantity', 'price_per_unit', 'date', 'created_at', 'updated_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductEntry, ProductEntryAdmin)
