import datetime

balance = 0.00

transhistory = []

def checkbal():
    input(
f"""\n--------------------------------
Your balance is ${balance:.2f}!
Press enter to continue.
--------------------------------
"""
    )

def removebalance(amount):
    global balance
    if balance >= amount:
        balance = balance - amount
        input(
f"""
{amount:.2f} has been withdrawn.
Your new balance is: ${balance:.2f}
Press enter to continue.
"""
        )
    else:
        input(
f"""Insufficient funds. You're ${(amount - balance):.2f} short!
Press enter to continue.""")
    return balance

def withdraw():
    global balance
    while True:
        try:
            amount = int(input(
f"""
--------------------------------
Current Balance: ${balance:.2f}.
--------------------------------
How much money would you like to
withdraw?                       

 1: $5.00             4: $50.00

 2: $10.00            5: Custom

 3: $20.00              6: Back
--------------------------------
"""))
            break
        except ValueError:
            input("Please enter a number from 1 to 6. Press enter to retry.")
        
    if amount == 1:
        removebalance(5)
    elif amount == 2:
        removebalance(10)
    elif amount == 3:
        removebalance(20)
    elif amount == 4:
        removebalance(50)
    elif amount == 5:
        removebalance(100)
    elif amount == 6:
        while True:
            try:
                customamount = float(input("Enter amount: "))
            except ValueError:
                print("Please enter a number.")
            if customamount > balance:
                nobalance = input(
f"""
Insufficient funds. You're ${(customamount - balance):.2f} short!
Press enter to retry or press 1 to exit.

""")
                if nobalance == '1':
                    break
            else:
                balance -= customamount
                input(
f"""
{customamount:.2f} Withdrawn. Your new balance is: ${balance}.
"""
                )
    else:
        input("Please enter a number from 1 to 6.  Press enter to retry.")


def addbalance(amount):
    global balance
    balance += amount
    input(
f"""
${amount:.2f} has been deposited.
Your new balance is ${balance:.2f}
Press enter to continue.
""")

def deposit():
    global balance
    try:
        select = int(input(
f"""
--------------------------------
Current Balance: ${balance:.2f}
--------------------------------
Which note would you like to
deposit?                       

 1: $5.00             4: $50.00

 2: $10.00           5: $100.00

 3: $20.00              6: Back
--------------------------------
"""))
                
    except ValueError:
        input("Please enter a number from 1 to 6. Press enter to retry.")
    if select == 1:
        addbalance(5)
    elif select == 2:
        addbalance(10)
    elif select == 3:
        addbalance(20)
    elif select == 4:
        addbalance(50)
    elif select == 5:
        addbalance(100)
    elif select == 6:
        pass
    else:
        input("Please enter a number from 1 to 6. Press enter to retry.")
        
        
        

def menu():
    while True:
        try:
            selection = int(input(
"""\n--------------------------------
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
            input("Please enter a number from 1 to 5. Press enter to retry.")
        if selection == 1:
            checkbal()
        elif selection == 2:
            withdraw()
        elif selection == 3:
            deposit()
        elif selection == 4:
            transachist()
        elif selection == 5:
            break
        else:
            input("Please enter a number from 1 to 5. Press enter to retry.")
        
menu()