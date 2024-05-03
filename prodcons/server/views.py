import typing as t
from django.http import JsonResponse

from server.models import Product, ProductEntry
from server.use_cases import consolidated_products_entries as _consolidated_products_entries, consolidated_product_entries as _consolidated_product_entries
from server.services import ProductEntriesService


def products():
    # FIXME: This is a bad idea, we should never return all products at once
    return JsonResponse(Product.objects.all().values(), safe=True)


def product_by_id(product_id):
    # FIXME: If we have logic here, should it be here?
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
    res = _consolidated_product_entries(company_id, product_id, ProductEntriesService)
    return JsonResponse(res)


def consolidated_products_entries(company_id):
    res = _consolidated_products_entries(company_id, ProductEntriesService)
    return JsonResponse(res)
