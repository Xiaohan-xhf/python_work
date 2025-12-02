from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


make_coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# 導入到同一個項目文件夾裡面，pycharm才能更好地發揮作用

# user_choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

is_on =True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        make_coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # my weakness
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
# 總結：觀察方法特點，發現它們很多都是返回值或者返回T/F。
### 可以用T/F來作為條件控制程序是否繼續進行

# print(menu.find_drink(user_choice))
#
#
# if make_coffee.is_resource_sufficient(user_choice):
#     money_machine.process_coins()
#
#
# else:
#     print("Sorry there is not enough water.")