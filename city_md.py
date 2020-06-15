import random
from product_md import ProductCls


class CityCls:
    cities = []

    def __init__(self, name, has_warehouse_pr, has_bank_pr):
        self.name = name
        self.has_warehouse = has_warehouse_pr
        self.has_bank = has_bank_pr
        self.create_city_product_fn()

    @classmethod
    def create_city_fn(cls, cities_lst_pr):
        for item in cities_lst_pr:
            cls.cities.append(CityCls(item["name"], item["has_warehouse"], item["has_bank"]))

    def create_city_product_fn(self):
        self.city_products = []
        for product in ProductCls.products:
            self.city_products.append(CityProductCls(self, product))


class CityProductCls:
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.generate_rnd_price_fn()

    def generate_rnd_price_fn(self):
        self.price = random.randint(self.product.min_price, self.product.max_price)
