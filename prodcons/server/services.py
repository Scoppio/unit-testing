from server.models import ProductEntry


class ProductEntriesService:

    @classmethod
    def all_product_entries_for_company(cls, company_id):
        return ProductEntry.objects.filter(company_id=company_id).values()
