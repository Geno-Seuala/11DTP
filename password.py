def setpassword():
    """
    Asks the user to input a password and if it is eight numerical
    digits wrong the password is returned, else an error message
    is displayed.
    
    Returns: password - string

    """

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

    Returns: done - boolean (whether the user guessed the password)

    """

    count = 0
    while True:
        if count < 5:
            try:
                # Asks the user for an input and if it matches the
                # Password set previously then true is returned
                # So that the program can run .
                password = int(input("What is your password?: "))
                if password == correct:
                    done = True
                    break
                # Increments the amount of times the user has guessed
                # Incorrectly so that the user can be locked out
                # After a certain number of incorrect guesses.
                else:
                    count = count + 1
                    print("Wrong password")
                    print()
            # Prints an error message if the user inputs something
            # Other than a number so that the program will stay running
            # If another datatype is inputted.
            except ValueError:
                print("Please only enter numbers")
                print()
        # Locks the user out and returns false so that the program
        # Knows that the user has guesses incorrectly five times
        else:
            print("Sorry! You're locked out!")
            print()
            done = False
            break
    return done

# Runs the setpassword() function and stores its return in a variable
# So that it can be used later to reference the correct password.
correct = setpassword()


# A placeholder if statement that either grants the user access if
# The password is guessed an locks them out if it isn't.
# This is so that I can test if my program works.
if entersystem() == True:
    print("You are greanted access to really important things.")
else:
    print("You can not access the really important things.")