drinks = ['flat white', 'decaf', 'latte', 'cappuccino', 'hot chocolate']
order = []

name = str(input("Welcome to Bob's coffee shop! What is your name?"))
selection = input("Hello!", name, "! Press 1 to order a drink")
while True:
    if selection == "1":
        print("Fantastic", name, "! these are the drinks we offer:")
        print(drinks)
        drink = input("Please select a drink: ")
        while True:
            if drink in drinks:
                order.append(drink)
                print(drink, "added to order.")
                break
            else:
                print("Sorry!", drink "isnt available!")
        break
    else:
        pass
