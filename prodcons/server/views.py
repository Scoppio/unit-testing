import typing as t
from django.http import JsonResponse

from server.models import Product, ProductEntry


def products():
    return JsonResponse(Product.objects.all().values(), safe=True)


def product_by_id(product_id):
    return JsonResponse(Product.objects.get(id=product_id))


def create_product(request_data):
    product = Product.objects.create(**request_data)
    return JsonResponse(product)


def update_product(product_id, request_data):
    product = Product.objects.get(id=product_id)
    for key, value in request_data.items():
        setattr(product, key, value)
    product.save()
    return JsonResponse(product)


def delete_product(product_id):
    Product.objects.get(id=product_id).delete()
    return JsonResponse({})


def increase_product_quantity(company_id, product_id, quantity, price_per_unit):
    product_entry = ProductEntry.objects.create(company_id=company_id, product_id=product_id, quantity=quantity, price_per_unit=price_per_unit)
    return JsonResponse(product_entry)


def decrease_product_quantity(company_id, product_id, quantity, price_per_unit):
    product_entry = ProductEntry.objects.create(company_id=company_id, product_id=product_id, quantity=-quantity, price_per_unit=price_per_unit)
    return JsonResponse(product_entry)


def consolidated_product_entries(company_id, product_id):
    consolidated_product_entries = ProductEntry.objects.filter(company_id=company_id, product_id=product_id).values()
    consolidate_entries = {
        "total_quantity": sum([entry['quantity'] for entry in consolidated_product_entries]),
        "total_price": sum([entry['quantity'] * entry['price_per_unit'] for entry in consolidated_product_entries]),
        "product": Product.objects.get(id=product_id).name,
        "product_id": product_id,
    }
    return JsonResponse(consolidate_entries)


def consolidated_product_entries(company_id):
    consolidated_product_entries: t.List[ProductEntry] = ProductEntry.objects.filter(company_id=company_id).values()
    consolidate_entries = {}
    for entry in consolidated_product_entries:
        product_id = entry.product.id
        if product_id not in consolidate_entries:
            consolidate_entries[product_id] = {
                "total_quantity": 0,
                "total_price": 0,
                "product": entry.product.name,
                "product_id": product_id,
            }
        consolidate_entries[product_id]['total_quantity'] += entry['quantity']
        consolidate_entries[product_id]['total_price'] += entry['quantity'] * entry['price_per_unit']
