import os
import random
from constant_md import MENU_DIVIDER, GAME_TITLE, RANDOM_PERCENTAGE
from database_md import cities_lst, products_lst
from datetime import datetime, timedelta
from product_md import ProductCls
from city_md import CityCls
from encounter_md import EncounterCls


class GameManager:
    def __init__(self, firm_name_pr, *, shiphold_pr=50, ship_health_pr=100, **kwargs):
        self.firm_name = firm_name_pr
        self.cash = kwargs["cash"]
        self.debt = kwargs["debt"]
        self.cannons = kwargs["cannons"]
        self.bank = 0
        self.shiphold = 0
        self.max_shiphold = shiphold_pr
        self.ship_health = ship_health_pr
        self.current_date = datetime(1800, 1, 1)

        ProductCls.create_product_fn(products_lst)
        CityCls.create_city_fn(cities_lst)
        self.current_city = CityCls.cities[0]

    def start_up_fn(self):
        running = True
        while running:

            os.system("cls")

            print(MENU_DIVIDER)
            print(GAME_TITLE)
            print(MENU_DIVIDER)

            print("Firm Name: %s" % self.firm_name)
            print("Cash: {}".format(self.cash))
            print(f"Debt: {self.debt}")
            print("Cannon: %d" % self.cannons)
            print("City: %s" % self.current_city.name)
            # print("Date: {:%B %m %Y}".format(current_date))
            print("Date: {}".format(self.current_date.strftime("%B %d %Y")))
            print("Shiphold: %d" % self.shiphold)

            print(MENU_DIVIDER)

            print("City Products".center(20, "-"))
            self.display_product_fn()

            has_bank_string = ""
            if self.current_city.has_bank:
                has_bank_string = "V)isit the Bank,"
            print("MENU: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, {} E)xit".format(has_bank_string))

            menu_option = input("What is your option?")
            if menu_option == "l":
                self.current_city, self.current_date = self.leave_port_fn(CityCls.cities, self.current_date)
                self.check_price_change_fn()
                self.increase_debt_fn()
                pirates = EncounterCls(self)
            elif menu_option == "b":
                self.buy_fn()
            elif menu_option == "s":
                self.sell_fn()
            elif menu_option == "v" and self.current_city.has_bank:
                self.visit_bank_fn()
            elif menu_option == "e":
                running = False
            else:
                input("Wrong Choice")

    def leave_port_fn(self, cities_pr, date_pr):
        for idx, city in enumerate(cities_pr, 1):
            print("{}) {}".format(idx, city.name))

        select_city = input("Which city do you wish to go to?")
        date_pr += timedelta(days=10)
        return CityCls.cities[int(select_city) - 1], date_pr

    def display_product_fn(self):
        for idx, city_product in enumerate(self.current_city.city_products, 1):
            print(str(idx) + ") " + city_product.product.name + " --- " + str(city_product.price) + " --- " + str(
                city_product.product.ship_quantity))

    def check_price_change_fn(self):
        result = random.randint(0, 100)
        if result >= RANDOM_PERCENTAGE:
            for city_product in self.current_city.city_products:
                city_product.generate_rnd_price_fn()

    def increase_debt_fn(self):
        self.debt *= 1.15

    def visit_money_lender_fn(self):
        payback = input("How much do you wish to pay back")
        if int(payback) <= self.cash:
            self.debt -= int(payback)
            self.cash -= int(payback)
        borrow = input("How much do you wish to pay borrow")
        if int(borrow) <= self.cash * 10:
            self.debt += int(borrow)
            self.cash += int(borrow)

    def buy_fn(self):
        select_buy = input("Which product do you want to buy? (1-" + str(len(ProductCls.products)) + "), c)ancel :")
        if select_buy == "c":
            return

        city_product = self.current_city.city_products[int(select_buy) - 1]
        quantity_to_buy = int(input("How many " + city_product.product.name + "do you want to buy?"))
        cost_to_buy = city_product.price * quantity_to_buy

        if cost_to_buy <= self.cash:
            if self.shiphold + quantity_to_buy <= self.max_shiphold:
                self.cash -= cost_to_buy
                self.shiphold += quantity_to_buy
                city_product.product.ship_quantity += quantity_to_buy
            else:
                print("You don't have enough space.")
        else:
            print("You don't have enough money.")

    def sell_fn(self):
        select_sell = input("Which product do you want to sell? (1-" + str(len(ProductCls.products)) + "), c)ancel :")
        if select_sell == "c":
            return

        city_product = self.current_city.city_products[int(select_sell) - 1]
        quantity_to_sell = int(input("How many " + city_product.product.name + "do you want to buy?"))
        cost_to_sell = city_product.price * quantity_to_sell

        if quantity_to_sell <= city_product.product.ship_quantity:
            self.cash += cost_to_sell
            city_product.product.ship_quantity -= quantity_to_sell
            self.shiphold -= quantity_to_sell
        else:
            print("You don't have {} many to sell".format(city_product.product.name))

    def visit_bank_fn(self):
        input("How much to transfer to the bank?")
