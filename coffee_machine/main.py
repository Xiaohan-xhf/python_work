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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. ask the user to choose the kind of coffee

user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
off_button = False

# TODO: 3. Print report of resources
if user_choice == "report":
    print(f"water: {resources['water']}ml,\nmilk: {resources['milk']}ml,\ncoffee: {resources['coffee']}g,")

# TODO: 4. Check resources sufficient?

# TODO: 5. Process coins.


# TODO: 6. Check transaction successful?


# TODO: 7. Make Coffee.

