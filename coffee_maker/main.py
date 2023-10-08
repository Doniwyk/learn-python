from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
item = MenuItem
maker = CoffeeMaker()
money = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        break
    elif choice == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)
