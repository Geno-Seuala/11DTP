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
Current Balance: ${balance}.
--------------------------------
How much money would you like to
withdraw?                       

 1: $5.00             4: $50.00

 2: $10.00           5: $100.00

 3: $20.00            6: Custom
--------------------------------

"""))
    
        except ValueError:
            input("Please enter a number from 1 to 6. Press enter to retry.")
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
        while True:
            try:
                customamount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Please enter a number.")
        balance = balance - customamount
    else:
        input("Please enter a number from 1 to 6. Press enter to retry.")

def deposit():
    while True:
        try:
            selection = int(input(
"""
--------------------------------
Current Balance: ${balance[:2]}
--------------------------------
Which note(s) would you like to
deposit?                       

 1: $5.00             4: $50.00

 2: $10.00           5: $100.00

 3: $20.00              6: Exit
--------------------------------

"""
    ))
                
        except ValueError:
            input("Please enter a number from 1 to 6. Press enter to retry.")
            if select == 1:
                balance = balance + 5
            elif select == 2:
                balance = balance + 10
            elif select == 3:
                balance = balance + 20
            elif select == 4:
                balance = balance + 50
            elif select == 5:
                balance = balance + 100
            elif select == 6:
                break
            else:
                input("Please enter a number from 1 to 6. Press enter to retry.")
    
        
            

def menu():
    while True:
        try:
            selection = int(input(
"""--------------------------------
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
            tranhist()
        elif selection == 5:
            break
        else:
            input("Please enter a number from 1 to 5. Press enter to retry.")
        
menu()