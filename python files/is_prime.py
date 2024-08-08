password = str(input("Please enter your password: "))
if any(char.isdigit() for char in password) == True and any(char.isdigit() for char in password) == False and len(password) > 12:
    print("Your password has above 12 characters and contains both numbers and letters")
else:
    print("Your password is insecure as it does not contain at least 13 characters OR it does not contain both numbers and letters")