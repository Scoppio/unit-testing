from unittest.mock import patch
from server.use_cases import consolidated_products_entries, consolidated_product_entries
from collections import namedtuple


Product = namedtuple("Product", ["name", "id"])
ProductEntry = namedtuple("ProductEntry", ["product", "quantity", "price_per_unit"])


class FakeRepo:
    def __init__(self, data = None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def all_product_entries_for_company(self, company_id):
        return self.data

    def all_product_entries_on_a_single_product_for_company(self, *args):
        return self.data


class TestViews:

    @patch('server.services.ProductEntriesService', FakeRepo)
    def test_consolidated_data_on_empty_list_of_entries(self, fake_repo):
        company_id = 1
        res = consolidated_products_entries(company_id)
        assert res == {}

    def test_consolidate_data_when_there_are_multiple_entries(self):
        p = Product("spam", 1)
        pe1 = ProductEntry(p, 2, 5)
        pe2 = ProductEntry(p, 2, 5)

        result = {
            1: {
                "total_quantity": 2 * 2,
                "total_price": 2 * 2 * 5,
                "product": "spam",
                "product_id": 1,
            }
        }
        company_id = 1
        res = consolidated_products_entries(company_id, FakeRepo([pe1, pe2]))
        assert res == result

    def test_consolidate_product_entries_for_one_product_empty_list(self):
        company_id = 1
        product_id = 1
        res = consolidated_product_entries(company_id, product_id, FakeRepo())
        assert res == {}

    def test_consolidate_product_entries_for_one_product_with_some_values(self):
        company_id = 1
        p = Product("spam", 1)
        pe1 = ProductEntry(p, 2, 5)
        pe2 = ProductEntry(p, 2, 5)

        result = {
            "total_quantity": 2 * 2,
            "total_price": 2 * 2 * 5,
            "product": "spam",
            "product_id": 1,
        }

        res = consolidated_product_entries(company_id, p.id, FakeRepo([pe1, pe2]))
        assert res == result

