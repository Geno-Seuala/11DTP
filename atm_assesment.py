# Imports the datetime module so that the user knows WHEN transactions
# Are made on the account.
from datetime import datetime

# Defines variable balance as 0 so that it can be modified by the user.
balance = 0.00

# Creates an empty list that transactions will be stored in
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
        Bool  (grantaccess): Whether or not the user has guessed the code in
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
    """Prints the balance of the user's account so that the user can be aware
    of how much funds are in the account if they wish to deposit or withdraw
    any money.

    """
    # An input prompting the user to press enter once they have finished
    # Reading their balance so that the user isn't bombarded by a large menu
    # Screen when trying to read their balance meaning that the user has an
    # Easier time using the ATM.
    input(
        f"""\n--------------------------------
Your balance is ${balance:.2f}!
Press enter to continue.
--------------------------------
"""
    )


def removebalance(amount):
    """Checks if the users balance is greater or equal to the amount of money
    selected. If so then the amount is subtracted from the users balance and
    the transaction along with the date and time is appended to the transaction
    history. If the balance is greater, an error is raised.
    
    Args: Float (amount): 
    
    """
    # Initialises the balance variable so that it can be modified in a
    # Withdrawl.
    global balance
    # Checks if the user has enough money to make the withdrawl.
    if balance >= amount:
        # Subtracts the amount from the users balance.
        balance -= amount
        # Defines, formats, and constructs the withdrawl into a string.
        now = datetime.now()
        dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
        transaction = ("Withdrawl - " + "$" +
                       f"{amount:.2f}" + ' | ' + str(dateandtime))
        # Appends the transaction into the transaction history list.
        transactionhistory.append(transaction)
        # Uses an input statement to inform the user that the funds have
        # Been subtracted from the account and prints their remaining
        # Balance.
        input(
            f"""
{amount:.2f} has been withdrawn.
Your new balance is: ${balance:.2f}
Press enter to continue.
"""
        )
    # Prints an error message telling the user how much more money they
    # Need in order to make the withdrawl.
    else:
        input(
            f"""Insufficient funds. You're ${(amount - balance):.2f} short!
Press enter to continue.""")


def withdraw():
    """Presents the user with an interface asking which note that they
    would like to deposit into their account. The options vary (5, 10, 
    20, 50, 100, and a custom amount). This uses the remove balance()\
    function to deduct the funds and handle errors.
    
    """
    # Initialises the balance variable so that it can be modified in a
    # Withdrawl.
    global balance
    # A while loop so that errors can be handles effectiently.
    while True:
        try:
            # Prints the menu as an input statement and stores the users
            # Input in a variable
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
        # Displays an error message in an input clause and tells the
        # User how to input into the menu and grants them an opportunity
        # To retry.
        except ValueError:
            input("Please enter a number from 1 to 6. Press enter to retry.")

    # Uses the removebalance() function in order to deduct the funds
    # From the users balance.
    if amount == 1:
        removebalance(5)
    elif amount == 2:
        removebalance(10)
    elif amount == 3:
        removebalance(20)
    elif amount == 4:
        removebalance(50)
        # If '5' is selected, the user is prompted to enter a custom
        # Amount of funds to be deducted.
    elif amount == 5:
        while True:
            try:
                # Asks the user to enter an amount
                customamount = float(input("Enter amount: "))
            # Handles invalid inputs (non - floats)
            except ValueError:
                print("Please enter a number.")
                # If the amount exceeds the balance, an error message
                # Is displayed and the user is given another chance
                # To either enter a valid input or go back.
            if customamount > balance:
                nobalance = input(
                    f"""
Insufficient funds. You're ${(customamount - balance):.2f} short!
Press enter to retry or press 1 to exit.

""")
                # Brings the user back to the menu if '1' is inputted.
                if nobalance == '1':
                    break
            else:
                removebalance(customamount)
                break
    # Exits the withdrawl screen and print the main menu of the ATM.
    elif amount == 6:
        pass
    else:
        input("Please enter a $ amount. Press enter to retry.")


def addbalance(amount):
    """A predetermined about of money is added to the users balance and
    the transaction along with the date and time is appended to the transaction
    history.
    
    Args: float (amount)
    
    """
    # Initialises the balance variable so that it can be modified in a
    # Withdrawl.
    global balance
    # Amount is added to balance
    balance += amount
    # Message printed using an input telling the user that the money has
    # Been deposited into their account and displays their updated
    # Balance.
    input(
        f"""
${amount:.2f} has been deposited.
Your new balance is ${balance:.2f}
Press enter to continue.
""")
    # Defines, formats, and constructs the withdrawl into a string.
    now = datetime.now()
    dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
    transaction = ("Deposit - " + "$" +
                   f"{amount:.2f}" + ' | ' + str(dateandtime))
    # Appends the transaction into the transaction history list.
    transactionhistory.append(transaction)


def deposit():
    # Initialises the balance variable so that it can be modified in a
    # Withdrawl.
    global balance
    try:
        # Prints the menu as an input statement and stores the users
        # Input in a variable
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
    # If a non-integer value is inputted, an error message is displayed
    # And the user is given an oppurtunity to try again.
    except ValueError:
        input("Please enter a number from 1 to 6. Press enter to retry.")
    # Uses the addbalance() function in order to add the funds
    # To the users balance.
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
    # If '6' is inputted, the main menu of the ATM is printed.
    elif select == 6:
        pass
    # If an integer that isnt in rande 1-6 is entered, then an error
    # Message is displayed and the user is given another change
    # To enter a valid input.
    else:
        input("Please enter a number from 1 to 6. Press enter to retry.")


def transactionhist():
    """Itterates over a list of transactions. If there are none to
    itterate; an error telling the user that there are no transactions
    recorded and the main menu of the atm is printed once the error is
    dismissed.
    
    """
    # Checks if any transactions have been made, if there are then the
    # Lists of transactions is itterated through and printed so that the
    # User can view and manually verify the transactions that has taken
    # Place on their account.
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
    # Error message printed.
    else:
        input(
            """
You have no transactions to show.
Press enter to go back.       
""")


def menu():
    """A menu that runs once the user has entered the correct pin, here the
    user can select which of the five presented operations they would like the
    ATM to perform (Check balance, Withdraw Funds, Deposit Funds, Print
    Transaction History, Exit). Once the user selects one, the operation takes
    place and the function loops back so that the user can choose another
    option and continue using the ATM.

    """
    # Asks the user to enter their pin (3104) in order to verify that the right
    # Person is accessing the funds in the account.
    if pinwall(3104) == True:
        # A while loop so that the user can perform multiple operations and try
        # Again if an error occurs without the need to restart the program.
        while True:
            try:
                # Prints a nifty menu screen letting the user know which inputs
                # Correspond to which operations.
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
            # Handles non-integer inputs and prompts the user to only enter
            # Numbers from one to five. This is an input statement in order to
            # Give the user time to read and learn how to use the program.
            except ValueError:
                input("Please enter a number from 1 to 5. Press enter to retry.")
            # If 1 is selected, the checkbal() function is called to check the
            # Users account's balance.
            if selection == 1:
                checkbal()
            # If 2 is selected, the withdraw() function is called to remove
            # Funds From the users account.
            elif selection == 2:
                withdraw()
            # If 3 is selected, the deposit() function is called to add funds
            # To the users acocunt.
            elif selection == 3:
                deposit()
            # If 4 is selected, the transactionhist() function is called to
            # Itterate over all of the transactions that the user has made.
            elif selection == 4:
                transactionhist()
            # If 5 is selected, the user is printed a parting message with a
            # Display of their remaining balance rounded to two d.p and the
            # Program exits.
            elif selection == 5:
                print(
                    f"See you soon! Your remaining balance is ${balance:.2f}")
                break
            # If an integer that isn't in range 1 to 5 is inputted,
            # Then the user is asked to Only enter valid inputs and is prompted
            # to press enter in order To retry so that the user can correctly
            # Use the ATM's menu.
            else:
                input("Please enter a number from 1 to 5. Press enter to retry.")

# Runs the program.
menu()
