from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu_list = Menu()
payment = MoneyMachine()

keep_ordering = True

while keep_ordering:
    choice = input(f"What would you like? {menu_list.get_items()}: ").lower()

    if choice == "report":
        coffee_machine.report()
        payment.report()
    elif choice == "latte":
        choice = menu_list.find_drink(choice)
        if coffee_machine.is_resource_sufficient(choice):
            if payment.make_payment(choice.cost):
                coffee_machine.make_coffee(choice)
    elif choice == "espresso":
        choice = menu_list.find_drink(choice)
        if coffee_machine.is_resource_sufficient(choice):
            if payment.make_payment(choice.cost):
                coffee_machine.make_coffee(choice)
    elif choice == "cappuccino":
        choice = menu_list.find_drink(choice)
        if coffee_machine.is_resource_sufficient(choice):
            if payment.make_payment(choice.cost):
                coffee_machine.make_coffee(choice)
    else:
        print("Machine is shutting down....")
        keep_ordering = False

