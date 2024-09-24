import random


def asknum():
    '''
    Asks the user to enter a number from one to five, raises a
    value error if the users input is either not a whole number
    or from 1-5
    '''

    while True:
        try:
            number = int(input("Please pick a number from 1-5: "))
            if number > 0 and number < 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Whoops! Remember your number must both")
            print("be from one to five and a whole number")
    return number


def askquestion():
    '''
    Asks the user to enter a value from 1 to 5, if the number 
    that the user has entered does not match a randomly generated
    number from one to five, the user is asked once more to guess 
    the number. This repeats the process three times untill the
    user is asked to enter a DIFFERENT number. If the user guesses 
    the number correctly, another number is randomly generated
    and the process erpeats untill the user enters five numbers 
    correctly. Then a congratulations message will be displayed.
    '''

    count = 0
    random_number = random.randint(1, 5)
    while True:
        numinput = asknum()
        if count < 2:
            if numinput == random_number:
                print("Good job!")
                break
            else:
                print()
                print("Try agian")
                count = count + 1
        elif count == 2:
            if numinput == random_number:
                print("Good job!")
                break
            else:
                print()
                print("  Whoops! You're out of turns!  ")
                print("A new number has been generated.")
                print()
                count = 0
                random_number = random.randint(1, 5)

# Prints a nifty title screen


print("---------------------------------------")
print()
print("      Welcome to the number game!      ")
print("           What is your name?          ")
print()
print("---------------------------------------")

# Asks the user for their name. (Name must contain letters)

while True:
    name = input('Please input a username: ')
    if any(char.isalpha() for char in name) == False:
        print("Invalid name! please use letters.")
        print("")
    else:
        break


# Greets the user using their name and briefly explains the game

print("------------------------------------------------------")
print()
print("   Hello!", name, "! and welcome to the number game!  ")
print()
print("in this game you will guess a number from one to five,")
print()
print("   If you can not guess the number in three turns,    ")
print("   a new number will be generated for you to guess    ")
print()
print("       there will be five rounds of guessing.         ")
print()
print("                     Good Luck!                       ")
print()
print("------------------------------------------------------")

# Uses previously defined functions to run five rounds of the game
roundcount = 0
while True:
    if roundcount < 4:
        askquestion()
        print("Good job! Time for round", roundcount + 2, "!")
        print()
        roundcount = roundcount + 1
    else:
        askquestion()
        break

# Prints an end screen to the user telling them how amazing They are

print("-------------------------------------------")
print()
print("Congrats! You have beaten the numbers game.")
print("          (press enter to close)           ")
print()
print("-------------------------------------------")

input()
