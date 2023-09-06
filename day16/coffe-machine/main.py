from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
choice = "latte"
drink = Menu().find_drink(choice)
print(drink.cost)
