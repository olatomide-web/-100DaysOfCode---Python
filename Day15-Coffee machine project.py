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



resources = {"water" : 300, "milk" : 200, "coffee" : 100}
profit = 0







def is_resource_sufficient(order_ingredients):
    
    resources_is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            resources_is_enough = False
    return resources_is_enough
    


def process_coins():
    """returns the total from the coins inserted into the machine"""
    
    print("please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01


    return total

def is_transaction_successful(money_received, cost_of_drink):
    """returns True when the payment is accepted or False if the money
    is insufficient
    """

    if money_received >= (cost_of_drink):
        change = round(money_received - cost_of_drink, 2)
        print(f"Your change is ${change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry insufficent funds, you need more money to purchase drink.")
        return False




def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")



Machine_is_on = True

while Machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        Machine_is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"money : ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink_name = choice, order_ingredients = drink["ingredients"])
                
            
        














