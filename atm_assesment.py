from datetime import datetime

balance = 0.00

transactionhistory = []

def pinwall(code):
    """Prompts the user to enter a pin. If the users input matches the code
    set in the fuctions argument then True is returned, if the user guesses
    incorrectly, they are given two more chances before "access denied" is
    printed and false is returned from the function. This is to verify the
    user and make sure that the right person is accessing the funds of the
    users account.

    Args:
        Int (code): A code for the user to guess.

    Returns:
        Bool (grantaccess): Whether or not the user has guessed the code in
        three attempts.
    
    """
    pin = int(code)
    attemptcount = 0
    
    # Loop that runs three times or untill the user guesses the pin correctly.
    while attemptcount < 3:
        try:
            # Prompts the user to enter a pin
            attempt = int(input("Please enter your pin: "))
            # Returns True if the users guess is correct.
            if attempt == pin:
                grantaccess = True
                break
            # Lets the loop know that the user has made an incorrect guess and
            # Lets the user know how many attempts remain and prompts them to
            # Try again.
            else:
                attemptcount += 1
                print(
f"""Incorrect pin.
You have {3 - attemptcount} attempts left""")
        except ValueError:
            input(
"""Please enter a 4 digit numerical code.
Press enter to retry.""")
    # If the user has guesses the pin incorrectly thee times then False is
    # Returned and "Access denied" is printed.
    if attemptcount == 3:
        grantaccess = False
        print("Access denied.")
    return grantaccess
    
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
        balance -= amount
        now = datetime.now()
        dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
        transaction = ("Withdrawl - " + "$" +
                       f"{amount:.2f}" + ' | ' + str(dateandtime))
        transactionhistory.append(transaction)
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
                removebalance(customamount)
                break
    elif amount == 6:
        pass
    else:
        input("Please enter a $ amount. Press enter to retry.")


def addbalance(amount):
    global balance
    balance += amount
    input(
f"""
${amount:.2f} has been deposited.
Your new balance is ${balance:.2f}
Press enter to continue.
""")
    now = datetime.now()
    dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
    transaction = ("Deposit - " + "$" +
                   f"{amount:.2f}" + ' | ' + str(dateandtime))
    transactionhistory.append(transaction)


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


def transactionhist():
    if len(transactionhistory) >= 1:
        print(
"""\n----------------------------------------
             Transactions:              """)
        for transaction in transactionhistory:
            print(f"[{transaction}]")
        input(
            """
----------------------------------------
Press enter to go back.
"""
        )
    else:
        input(
"""
You have no transactions to show.
Press enter to go back.       
""")


def menu():
    if pinwall(3104) == True:
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
                transactionhist()
            elif selection == 5:
                print(f"See you soon! Your balance is ${balance:.2f}")
                break
            else:
                input("Please enter a number from 1 to 5. Press enter to retry.")


menu()
