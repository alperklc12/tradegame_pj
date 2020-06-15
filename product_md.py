import random


class ProductCls:
    products = []

    def __init__(self, name, min_price, max_price):
        self.name = name
        self.min_price = min_price
        self.max_price = max_price
        self.ship_quantity = 0
        self.warehouse_quantity = 0

    @classmethod
    def create_product_fn(cls, products_lst_pr):
        for item in products_lst_pr:
            cls.products.append(ProductCls(item["name"], item["min_price"], item["max_price"]))
