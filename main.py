MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino)
money = 0
contes = False


def the_coffee_machine(contes):
    cont = True
    global money
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO Print report.
    def menu_list():
        if order == "latte" or "cappuccino" or "espresso":
            water = MENU[order]['ingredients']['water']
            milk = MENU[order]['ingredients']['milk']
            coffee = MENU[order]['ingredients']['coffee']
            cost = MENU[order]['cost']
            listm = [water, milk, coffee, cost]
            return listm

    water1 = resources['water']
    milk1 = resources['milk']
    coffee1 = resources['coffee']
    resources_list = [water1, milk1, coffee1]

    if order == "report":

        print(f"Water: {resources_list[0]}\nMilk: {resources_list[1]}\nCoffee: {resources_list[2]}\nMoney: {money}$")

    else:

        # TODO Check resources sufficient?
        def check_resources():

            if resources_list[0] - menu_list()[0] > 0:
                if resources_list[1] - menu_list()[1] > 0:
                    if resources_list[2] - menu_list()[2] > 0:
                        return True
                    else:
                        return False

        # TODO Process coins.

        def coins():

            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            quarters *= 0.25
            dimes *= 0.1
            nickles *= 0.05
            pennies *= 0.01
            listc = [quarters, dimes, nickles, pennies]
            return listc

        # TODO Check transaction successful?
        def accept_coins():

            global money
            global contes
            global resources
            listc = coins()
            listm = menu_list()
            money_taken = listc[0] + listc[1] + listc[2] + listc[3]

            if money_taken >= listm[3]:
                change = round(money_taken - listm[3], 3)
                money += listm[3]
                resources["water"] -= menu_list()[0]
                resources["milk"] -= menu_list()[1]
                resources["coffee"] -= menu_list()[2]
                print(f"Here's {change}$ in change.")
                print(f"Here is your {order}. Enjoy!")
                contes = True
            else:
                print("Sorry that's not enough money. Money refunded.")

        # TODO Make Coffee.
        if check_resources():
            accept_coins()
            if contes:
                print(f"Here is your {order}. Enjoy!")
        else:
            print("Sorry there is not enough resources. ")

    while cont:

        the_coffee_machine(False)


the_coffee_machine(False)

