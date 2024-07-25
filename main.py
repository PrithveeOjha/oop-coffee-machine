from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffeeMaker.report())
        print(moneyMachine.report())
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.process_coins():
              coffeeMaker.make_coffee(drink)

