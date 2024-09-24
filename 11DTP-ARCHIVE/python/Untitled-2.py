def deposit():
    """Presents the user with an interface asking what amount that they
    would like to deposit into their account. The options vary (5, 10, 
    20, 50, 100, and a custom amount). This uses the remove balance()\
    function to deduct the funds and handle errors.
    
    """
    balance = 2
    while True:
        while True:
            try:
                # Prints the menu as an input statement and stores the users
                # Input in a variable
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
                input("""Please enter a value from 1 - 6.
Press enter to retry.""")
        # Uses the addbalance() function in order to add the funds
        # To the users balance.
        if amount == 1:
            addbalance(5)
            break
        elif amount == 2:
            addbalance(10)
            break
        elif amount == 3:
            addbalance(20)
            break
        elif amount == 4:
            addbalance(50)
            break
        elif amount == 5:
            addbalance(100)
            break
        # If '6' is inputted, the main menu of the ATM is printed.
        elif amount == 6:
            break
        # If an integer that isnt in rande 1-6 is entered, then an error
        # Message is displayed and the user is given another change
        # To enter a valid input.
        else:
            input("""\nPlease enter a number from 1 - 6. 
Press enter to retry.""")
        
deposit()