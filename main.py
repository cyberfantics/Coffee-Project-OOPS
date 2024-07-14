from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine
import os

coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()
is_on = True

os.system("cls")
coffee_maker.report()
money_maker.report()

while is_on:
    option = Menu.get_items
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_on = False
        
    elif choice == "report":
        coffee_maker.report()
        money_maker.report()