from menu import resources, MENU

def display_prompt():
    print("What would you like?")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")

def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"{item} is not available")
            return False
    return True

def process_coins(drink):
    print("Please enter coins")
    rupee_10 = int(input("How many 10 rupee notes?"))
    rupee_20 = int(input("How many 20 rupee notes?"))
    rupee_50 = int(input("How many 50 rupee notes?"))
    rupee_100 = int(input("How many 100 rupee notes?"))
    rupee_200 = int(input("How many 200 rupee notes?"))
    total_cash = (rupee_10 * 10) + (rupee_100 * 100) + (rupee_20 * 20) + (rupee_50 * 50) + (rupee_200 * 200)

    if total_cash >= MENU[drink]['cost']:
        return_cash = total_cash - MENU[drink]['cost']
        print(f"Your return cash is {return_cash}")
        resources['money'] += MENU[drink]['cost']
        make_coffee(drink)
    else:
        print("Not enough money")

def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Your {drink} is ready")

display_prompt()
user_input = input("")

if user_input == "off":
    print("End execution")
elif user_input == "report":
    for item, quantity in resources.items():
        print(f"{item}: {quantity}")
elif user_input in ["espresso", "latte", "cappuccino"]:
    if check_resources(user_input):
        process_coins(user_input)
