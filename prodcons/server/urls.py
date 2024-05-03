from django.urls import path

from . import views

urlpatterns = [
    path("products/consolidate", views.consolidated_product_entries, name="consolidated_product_entries"),
    path("products/consolidate/<int:product_id>", views.consolidated_product_entries, name="consolidated_product_entries"),
    
    path("products/<int:product_id>/decrease", views.decrease_product_quantity, name="decrease_product_quantity"),
    path("products/<int:product_id>/increase", views.increase_product_quantity, name="increase_product_quantity"),
    
    path("products", views.products, name="products"),
    path("products/<int:product_id>", views.product_by_id, name="product_by_id"),
    path("products", views.create_product, name="create_product"),
    path("products/<int:product_id>", views.update_product, name="update_product"),
    path("products/<int:product_id>", views.delete_product, name="delete_product"),
]
