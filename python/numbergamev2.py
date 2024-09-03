import random


def asknum(range):
    '''
    Asks the user to enter a number from one to five, raises a
    value error if the users input is either not a whole number
    or from 1-20
    '''

    while True:
        try:
            number = int(input(f"Please pick a number from 1 - {range}: "))
            if number > 0 and number < range:
                break
            else:
                raise ValueError
        except ValueError:
            print("Whoops! Remember your number must both")
            print("be from one to", range, "and a whole number")
    return number


def askquestion(range1):
    '''
    '''

    count = 0
    random_number = random.randint(1, range1)
    while True:
        numinput = asknum(range1)
        if numinput == random_number:
            print("Good job!")
            break
        elif numinput > random_number:
            print()
            print(numinput, "Is higher than than the mystery number")
        else:
            print()
            print(numinput, "Is lower than than the mystery number")


print("---------------------------------------")
print()
print("      Welcome to the number game!      ")
print("           What is your name?          ")
print()
print("---------------------------------------")

while True:
    name = input('Please input a username: ')
    if any(char.isalpha() for char in name) == False:
        print("Invalid name! please use letters.")
        print("")
    else:
        break

print("------------------------------------------------------")
print()
print("   Hello!", name, "! and welcome to the number game!  ")
print()
print("      you will guess a number from one to twenty,     ")
print()
print("        After you guess the number correctly,         ")
print("   a new number will be generated for you to guess    ")
print("         but this time from one to one hundred        ")
print()
print()
print("                     Good Luck!                       ")
print()
print("------------------------------------------------------")

input("Press any key to continue: ")
askquestion(20)

askquestion(100)

print("-------------------------------------------")
print()
print("Congrats! You have beaten the numbers game.")
print("          (press enter to close)           ")
print()
print("-------------------------------------------")

input()
