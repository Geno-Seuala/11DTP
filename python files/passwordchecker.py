try:
    password = str(input("Please enter your password: "))
    if any(char.isdigit() for char in password) == False:
        raise TypeError
    elif len(password) < 11:
        raise KeyError
    elif any(char.isupper() for char in password) == False:
        raise IndexError
    else:
        print("Your password is strong")
except TypeError:
    print("There are no numbers in your password")
except KeyError:
    print("Please enter a password with at least 12 characters")
except IndexError:
    print("Your password has no capital letters")


