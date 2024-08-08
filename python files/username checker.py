try:
    username = input('Please input a username: ')
    for char in username:
        if char.isdigit == False and char.isalpha == False:
            raise KeyError
        else:
            break
print("Nice username!")

except KeyError:
    print("Your username contains an invalid character")