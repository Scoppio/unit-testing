import typing as t


def consolidated_products_entries(company_id, repo_service):
    _c: t.List = repo_service.all_product_entries_for_company(company_id)
    consolidate_entries = {}
    for entry in _c:
        product_id = entry.product.id
        if product_id not in consolidate_entries:
            consolidate_entries[product_id] = {
                "total_quantity": 0,
                "total_price": 0,
                "product": entry.product.name,
                "product_id": product_id,
            }
        consolidate_entries[product_id]['total_quantity'] += entry.quantity
        consolidate_entries[product_id]['total_price'] += entry.quantity * entry.price_per_unit

    return consolidate_entries


def consolidated_product_entries(company_id, product_id, repo_service):
    consolidated_product_entries = repo_service.all_product_entries_on_a_single_product_for_company(company_id, product_id)
    if not consolidated_product_entries:
        return {}

    consolidate_entries = {
        "total_quantity": sum([entry.quantity for entry in consolidated_product_entries]),
        "total_price": sum([entry.quantity * entry.price_per_unit for entry in consolidated_product_entries]),
        "product": consolidated_product_entries[0].product.name,
        "product_id": product_id,
    }
    return consolidate_entries
