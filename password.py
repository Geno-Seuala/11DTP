def setpassword():
    """ Asks the user to input a password and if it is eight numerical
    digits wrong the password is returned, else an error message
    is displayed.
    
    Arguments: password input
    
    Returns: password input """

    while True:
        try:
            # Prompts the user to enter a password at least eight
            # Numerical digits so that it can be Stored and guessed 
            # Later on
            password = int(input("Please enter a password: "))
            if len(str(password)) < 8:
                print("Please use at least 8 characters with no spaces")
            else:
                break
        except ValueError:
            print("Please use at least 8 numbers with no spaces")
    return password

def entersystem():
    """
    Asks the user for an input and returns as True if the input
    matches their password.

    Arguments: Password guess.

    Returns: True if they guess it correctly. False if they don't after
    5 attempts
    """
    count = 0
    while True:
        if count < 5:
            try:
                # Asks the user for an input and if it matches the
                # Password set previously then true is returned
                # So that the program can run 
                password = int(input("What is your password?: "))
                if password == correct:
                    done = True
                    break
                else:
                    count = count + 1
                    print("Wrong password")
                    print()
            except ValueError:
                print("Please only enter numbers")
                print()
        else:
            print("Sorry! You're locked out!")
            print()
            done = False
            break
    return done

correct = setpassword()

print(entersystem())