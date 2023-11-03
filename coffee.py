MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def check_resource(selected_product):
    ingredients = MENU[selected_product]["ingredients"]
    lista = []
    for i in ingredients:
        if resources[i] < ingredients[i]:
            lista.append(i)
    return lista


def sum_money(quarters, dimes, nickels, pennies):
    user_money = quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY
    return user_money


def check_money(user_money):
    if user_money >= MENU[selected_product]["cost"]:
        change = round(user_money - MENU[selected_product]["cost"], 2)
        return change
    else:
        return -1


def update_report(selected_product):
    ingredients = MENU[selected_product]["ingredients"]
    for i in ingredients:
        resources[i] -= ingredients[i]
    resources["money"] += MENU[selected_product]["cost"]


while True:
    selected_product = input(
        "Hello! What would you like to order? (espresso/latte/cappuccino)\n>"
    ).lower()
    if selected_product == "off":
        print("Coffee machine turned off. See you again later!")
        break
    if selected_product == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}"
        )
        continue
    checked = check_resource(selected_product)
    if len(checked) == 0:
        print("Please insert coins.")
        quarters = float(input("> how many quarters: "))
        dimes = float(input("> how many dimes: "))
        nickels = float(input("> how many nickels: "))
        pennies = float(input("> how many pennies: "))
        user_money = sum_money(quarters, dimes, nickels, pennies)
        change = check_money(user_money)
        if change > 0:
            update_report(selected_product)
            print(f"Here is ${change} in change.")
            print(f"Here is your {selected_product} ☕️. Enjoy!")
        elif change == 0:
            update_report(selected_product)
            print(f"Here is your {selected_product}. Enjoy!")
        else:
            print("Not enough coins. Money refunded.")
    else:
        print(f"Not enough: {', '.join(checked)}.")
