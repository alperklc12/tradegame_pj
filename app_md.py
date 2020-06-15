from game_manager_md import GameManager


def welcome_massage_fn():
    print("Welcome to python Priate Trader")


def get_firm_name_fn():
    # firm_name_lc = input("Please enter your firm name: ")
    return "Test Firm"


def starting_options_fn():
    # starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons no debt")
    starting_options = "1"
    if starting_options == "1":
        cash_lc = 250
        debt_lc = 250
        cannons_lc = 0
    else:
        cash_lc = 0
        debt_lc = 0
        cannons_lc = 10
    return cash_lc, debt_lc, cannons_lc


# Start Game
welcome_massage_fn()
firm_name = get_firm_name_fn()

cash, debt, cannons = starting_options_fn()
game = GameManager(firm_name, cash=cash, debt=debt, cannons=cannons)
game.start_up_fn()
