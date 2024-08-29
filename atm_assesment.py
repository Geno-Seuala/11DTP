# Imports the datetime module so that the user knows WHEN transactions
# Are made on the account.
from datetime import datetime

# Defines variable balance as 0 so that it can be modified by the user.
# When withdrawls and deposits are made.
balance = 0.00

# Creates an empty list so that the transactions can be stored within
# The program.
transactionhistory = []


def pinwall(code):
    """Prompts the user to enter a pin. If the users input matches the
    code set in the fuctions argument then True is returned, if the user
    guesses incorrectly, they are given two more chances before "access 
    denied" is printed and false is returned from the function. This is 
    to verify the user and make sure that the right person is accessing 
    the funds of the users account.

    Args:
        Int (code): A code for the user to guess.

    Returns:
        Bool  (grantaccess): Whether or not the user has guessed the 
        code in three attempts.

    """
    pin = int(code)
    nobalance = 0
    attemptcount = 0

    # Loop that runs three times or untill the user guesses the pin 
    # Correctly.
    while attemptcount < 3:
        try:
            # Prompts the user to enter a pin
            attempt = int(input("Please enter your pin: "))
            # Returns True if the users guess is correct.
            if attempt == pin:
                grantaccess = True
                break
            # Lets the loop know that the user has made an incorrect 
            # Guess and lets the user know how many attempts remain and 
            # Prompts them to try again.
            else:
                attemptcount += 1
                print(
                    f"""Incorrect pin.
You have {3 - attemptcount} attempts left""")
        except ValueError:
            input(
                """Please enter a 4 digit numerical code.
Press enter to retry.""")
    # If the user has guesses the pin incorrectly thee times then False 
    # Is Returned and "Access denied" is printed.
    if attemptcount == 3:
        grantaccess = False
        print("Access denied.")
    return grantaccess


def checkbal():
    """Prints the balance of the user's account so that the user can be 
    aware of how much funds are in the account if they wish to deposit 
    or withdraw any money.

    """
    # An input prompting the user to press enter once they have finished
    # Reading their balance so that the user isn't bombarded by a large 
    # Menu screen when trying to read their balance meaning that the 
    # user has an easier time using the ATM.
    input(
        f"""\n--------------------------------
Your balance is ${balance:.2f}!
Press enter to continue.
--------------------------------
"""
    )


def removefrombalance(amount):
    """Checks if the users balance is greater or equal to the amount of 
    moneyselected. If so then the amount is subtracted from the users 
    balance and the transaction along with the date and time is appended
    to the transactionhistory. If the balance is greater, an error is 
    raised.
    
    Args: Float (amount): 
    
    """
    # Initialises the users balance so that it can be modified in a
    # Withdrawl.
    global balance
    # Checks if the user has enough money to make the withdrawl. so that
    # The user can't withdrawl more than they have.
    if balance >= amount:
        # Subtracts the amount from the users balance.
        balance -= amount
        # Defines, formats, and constructs the withdrawl amount and
        # Date/time into a string. So that the user can see later that
        # A withdrawl has been made in their account.
        now = datetime.now()
        dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
        transaction = ("Withdrawl - " + "$" +
                       f"{amount:.2f}" + ' | ' + str(dateandtime))
        # Appends the transaction into the transaction history list.
        # So that it is stored within the program
        transactionhistory.append(transaction)
        # Uses an input statement to inform the user that the funds have
        # Been subtracted from the account and prints their remaining
        # Balance so that the user knows that all is okay.
        input(
            f"""
{amount:.2f} has been withdrawn.
Your new balance is: ${balance:.2f}
Press enter to continue.
"""
        )
    # Prints an error message telling the user how much more money they
    # Need in order to make the withdrawl so the user isn't confused as
    # To why an error has occured making the program easier to use.
    else:
        input(
            f"""Insufficient funds. You're ${(amount - balance):.2f}
short! Press enter to continue.""")


def withdraw():
    """Presents the user with an interface asking what amount that they
    would like to withdraw from their account. The options vary (
    $5, $10, $20, $50, and a custom amount). This uses the remove 
    balance() function to deduct the funds and handle errors.
    
    """
    # A while loop so that errors can be handled effectively without the
    # Program stopping or crashing. This makes the program robust and
    # Harder to break and crash
    while True:
        amount = 0
        try:
            # Prints the menu as an input statement and stores the users
            # Input in a variable so that the ATM knows how much the
            # User wants to withdraw from their account.
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
        # To retry so that the user can tell what has gone wrong and how
        # To fix it.
        except ValueError:
            input("""Please enter a value from 1 - 6.
Press enter to retry.""")

    # Uses the removefrombalance() function in order to deduct the funds
    # From the users balance.
    if amount == 1:
        removefrombalance(5)
    elif amount == 2:
        removefrombalance(10)
    elif amount == 3:
        removefrombalance(20)
    elif amount == 4:
        removefrombalance(50)
        # If '5' is selected, the user is prompted to enter a custom
        # Amount of funds to be deducted.
    elif amount == 5:
        while True:
            while True:
                nobalance = 0
                customamount = 0
                try:
                    # Asks the user to enter an amount of money to
                    # Withdraw so that they can withdraw custom amounts 
                    # Of money as opposed to the preset $5, $10, $20, 
                    # And $50 options
                    customamount = float(input("Enter amount: "))
                    
                    if customamount <= 0:
                        input("""\nPlease enter a positive number.
Press enter to retry.
""")
                
                    else:
                        break
                    
                # Handles invalid inputs (non - floats) so that the 
                # Program doesn't try to do maths with a string meaning 
                # The program doesnt crash. The user is instead told 
                # What went wrong in simple words and given another
                # Chance so that the program is accesible and robust 
                # (it doesn't crash)
                except ValueError:
                    input("""\nPlease enter a number.
Press enter to try again.
""")
            

                    # If the amount exceeds the balance, an error 
                    # Message is displayed and the user is given another
                    # Chance to either enter a valid input or go back.
            if customamount > balance:
                nobalance = input(
                    f"""
Insufficient funds. You're ${(customamount - balance):.2f} short!
Press enter to retry or press 1 to exit.

""")
                    # Brings the user back to the menu if '1' is 
                    # inputted. So they aren't forced to withdraw if 
                    # They choose this option.
            if nobalance == '1':
                break
            elif balance >= customamount:
                removefrombalance(customamount)
                break
    # Exits the withdrawl screen and print the main menu of the ATM. So
    # That further modifications can be made to the users balance/
    elif amount == 6:
        pass
    else:
        input("""Please enter a value from 1 - 6.
Press enter to retry.""")


def addtobalance(amount):
    """A predetermined about of money is added to the users balance and
    the transaction along with the date and time is appended to the 
    transaction history.
        
        Args: float (amount)
        
    """
    # Initialises the balance variable so that it can be modified in a
    # Withdrawl.
    global balance
    # Amount is added to balance so that it is put into the users
    # Account and the user can spend the funds.
    balance += amount
    # Message printed using an input telling the user that the money has
    # Been deposited into their account and displays their updated
    # Balance so that the user does not have to keep track of their
    # Funds.
    input(
        f"""
${amount:.2f} has been deposited.
Your new balance is ${balance:.2f}
Press enter to continue.
""")
        # Defines, formats, and constructs the deposit amount and
        # Date/time into a string. So that the user can see later that
        # A deposit has been made in their account.
    now = datetime.now()
    dateandtime = now.strftime("%d.%m.%Y %H:%M:%S")
    transaction = ("Deposit - " + "$" +
                   f"{amount:.2f}" + ' | ' + str(dateandtime))
    # Appends the transaction into the transaction history list. So that
    # The user can keep track of the activity on their account through
    # Stored data within the program.
    transactionhistory.append(transaction)


def deposit():
    """Presents the user with an interface asking what amount that they
    would like to deposit into their account. The options vary (5, 10, 
    20, 50, 100, and a custom amount). This uses the remove balance()\
    function to deduct the funds and handle errors.
    
    """
    while True:
        while True:
            amount = 0
            try:
                # Prints the menu as an input statement and stores the
                # Users Input in a variable
                amount = int(input(
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
                break
        # If a non-integer value is inputted, an error message is 
        # Displayed and the user is given an oppurtunity to try again.
            except ValueError:
                input("""Please enter a number from 1 - 6. 
Press enter to retry.""")
        # Uses the addtobalance() function in order to add the funds
        # To the users balance.
        if amount == 1:
            addtobalance(5)
            break
        elif amount == 2:
            addtobalance(10)
            break
        elif amount == 3:
            addtobalance(20)
            break
        elif amount == 4:
            addtobalance(50)
            break
        elif amount == 5:
            addtobalance(100)
            break
        # If '6' is inputted, the main menu of the ATM is printed.
        elif amount == 6:
            break
        # If an integer that isnt in rande 1-6 is entered, then an error
        # Message is displayed and the user is given another change
        # To enter a valid input.
        else:
            input("""Please enter a number from 1 - 6.
Press enter to retry.""")


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
        input("""
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
    """A menu that runs once the user has entered the correct pin, here
    the user can select which of the five presented operations they 
    would like the ATM to perform (Check balance, Withdraw Funds, 
    Deposit Funds, Print Transaction History, Exit). Once the user 
    selects one, the operation takes place and the function loops back 
    so that the user can choose another option and continue using the 
    ATM.

    """
    # Asks the user to enter their pin (3104) in order to verify that 
    # The right person is accessing the funds in the account.
    if pinwall(3104) == True:
        # A while loop so that the user can perform multiple operations 
        # And try again if an error occurs without the need to restart 
        # The program.
        while True:
            try:
                # Prints a nifty menu screen letting the user know 
                # Which inputs correspond to which operations. it takes
                # An integer as an input and makes a selection if the
                # Input is in range 1-5, else an error message is
                # Printed so that the user know swhat has gone wrong
                # And how to fix it. The user is then granted another
                # Chance.
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
            # Handles non-integer inputs and prompts the user to only 
            # Enter numbers from one to five. This is an input statement
            # In order to give the user time to read and learn how to 
            # Use the program.
            except ValueError:
                input("""Please input a value from 1 - 5. 
Press enter to retry.
""")
            # If 1 is selected, the checkbal() function is called to 
            # Check the users account's balance.
            if selection == 1:
                checkbal()
            # If 2 is selected, the withdraw() function is called to 
            # Remove funds From the users account.
            elif selection == 2:
                withdraw()
            # If 3 is selected, the deposit() function is called to 
            # Add funds to the users acocunt.
            elif selection == 3:
                deposit()
            # If 4 is selected, the transactionhist() function is called
            # To itterate over all of the transactions that the user has 
            # Made so that the user is aware of the activity that has
            # Happened on their account.
            elif selection == 4:
                transactionhist()
            # If 5 is selected, the user is printed a parting message 
            # With a display of their remaining balance rounded to two 
            # Decimal places and the program exits.
            elif selection == 5:
                print(
                    f"Goodbye! Your balance is now ${balance:.2f}")
                break
            # If an integer that isn't in range 1 to 5 is inputted,
            # Then the user is asked to Only enter valid inputs and is 
            # Prompted to press enter in order to retry so that the user
            # Can correctly use the ATM's menu.
            else:
                input("""Please enter a value from 1 - 5.
Press enter to retry.
""")

# Prompts the program to start so that the user can view and configure
# The balance of their account.
menu()
