def deposit():
    balance = 2
    while True:
        while True:
            try:
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
            except ValueError:
                input("""Please enter a value from 1 - 6.
Press enter to retry.""")
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
        elif amount == 6:
            break
        else:
            input("""\nPlease enter a number from 1 - 6. 
Press enter to retry.""")
        
deposit()