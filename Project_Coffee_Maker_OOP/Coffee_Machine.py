from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()  # TODO - am creat obiectul pentru a accesa .report() din Clasa MoneyMachine(): imi returneaza Money: $value
coffee_maker = CoffeeMaker()  ##TODO - am creat obiectul pentru a accesa .report() din Clasa CoffeeMaker(): imi returneaza Water: 300ml, Milk: 200ml, Coffee: 100g(aici, valoriile by default)
menu = Menu()  # TODO - am creeat obiectul pentru a avea acces la functia get_items din interiorul while loop
do_we_have_that_drink = True  # TODO by default True


while do_we_have_that_drink:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == 'off':
        do_we_have_that_drink = False
    elif choice == 'report':
        coffee_maker.report() #TODO accesam report din Class CoffeeMaker ce imi returneaza Water: 300ml, Milk: 200ml, Coffee: 100g
        money_machine.report() #TODO accesam report din Class MoneyMachine ce imi returneaza Money: $value
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


