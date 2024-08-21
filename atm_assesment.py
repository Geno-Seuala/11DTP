import datetime

balance = 0.00

def checkbal():
    print(
f"""
Your balance is ${balance}!
""" 
    )

def withdraw():
    while True:
        try:
            amount = int(input(
f"""
--------------------------------
Current Balance: ${balance}
--------------------------------
How much money would you like to
withdraw?

1: $5.00               4: $50.00

2: $10.00             5: $100.00

3: $20.00              6: Custom

"""))
    
        except ValueError:
            print("Please enter a number from 1 to 6.")
        break
    
    if amount == 1 and balance >= 5:
        balance = balance - 5
    elif amount == 2 and balance >= 10:
        balance = balance - 10
    elif amount == 3 and balance >= 20:
        balance = balance - 20
    elif amount == 4 and balance >= 50:
        balance = balance - 50
    elif amount == 5 and balance >= 100:
        balance = balance - 100
    elif amount == 6:
        customamount = 
    else:
        print("Please enter a number from 1 to 6.")
    

def menu():
    while True:
        try:
            selection = int(input(
"""
--------------------------------
Welcome to Westlake's GBNZ ATM! 
Please select an option below:
--------------------------------
1: Check Balance
2: Withdraw Funds
3: Deposit Funds
4: Print Transaction History
5: Exit
--------------------------------
"""
            ))
        except ValueError:
            print("Please enter a number from 1 to 5.")
        if selection == 1:
            checkbal()
        elif selection == 2:
            withdraw()
        elif selection == 3:
            deposit()
        elif selection == 4:
            tranhist()
        elif selection == 5:
            break
        else:
            print("Please enter a number from 1 to 5.")
        
menu()