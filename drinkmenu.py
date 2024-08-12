from datetime import date
import random

today = date.today()

drinks = ['flat white', 'decaf', 'latte', 'cappuccino', 'hot chocolate']
order = []

name = str(input("Welcome to Bob's coffee shop! What is your name?; "))


def randomprice():
    """
    Generates a random price from $4 to $6.50 to sell coffee at
    """
    prices = [4.50, 6, 3.50, 5, 4, 5.50, 6.50]
    price = random.choice(prices)
    return price


# Prints drinks menu, user to input a drink and adds to order
while True:
    print("Hello!", name, "! Press 1 to order a drink,")
    print("press 2 to send order")
    selection = input()
    if selection == "1":
        print("Fantastic", name, "! these are the drinks we offer:")
        print(drinks)
        while True:
            drink = input("Please select a drink: ")
            if drink in drinks:
                order.append(drink)
                print(drink, "added to order.")
                break
            else:
                print(f"Sorry! {drink} isnt available!")

# Prints users reciept with their name, date order price and cafe name
    elif selection == "2":
        print("--------------------------------------")
        print("          ", today, name, "           ")
        print("--------------------------------------")
        print("                                      ")
        price1 = randomprice()
        print(order[0], " - $", price1)
# If there isnt another item on the order, it is skipped
        try:
            price2 = randomprice()
            print(order[1], " - $", price2)
        except:
            price2 = 0
        try:
            price3 = randomprice()
            print(order[2], " - $", price3)
        except:
            price3 = 0
        try:
            price4 = randomprice()
            print(order[3], " - $", price4)
        except:
            price4 = 0
        try:
            print()
            print("Total:", price1 + price2 + price3 + price4)
            print()
        except:
            pass
        print("--------------------------------------")
        print("          Bob's Coffee Shop           ")
        print("--------------------------------------")
        print()
        input("press any key to close")
    else:
        print()
        print("Only select 1 or 2")
        print()
