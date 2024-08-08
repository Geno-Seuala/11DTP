import random

def title():

    '''
    Prints a title screen
    '''

    print("_______________________________________")
    print()
    print("      Welcome to the number game!      ")
    print()
    print("_______________________________________")

def asknum():

    '''
    Asks the user to enter a number from one to five
    '''

    while True:
        try:
            number = int(input("Please pick a number from 1-5: "))
            if number > 0 and number < 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Whoops! Remember your number has to be from one to five and a whole number")
    return number

def question():

    '''
    Asks the user to enter a number from one to five and outputs True if it matches
    with a randomly generated number from one to five
    '''

    number = genrandom5()
    if asknum() == number:
        Q1 = True
    else:
        Q1 = False

    return
def genrandom5():

    '''
    Generates a (random) number from 1-5
    '''

    number = random.randint(1, 5)
    return number

# Asks the user to pick a number from one to five and check whether or not it matches a randomly generated number from one to five

def askquestion():

    '''
    Asks the user to enter a value from 1 to 5, if the number that the user has entered does not match a randomly generated
    number from one to five, the user is asked once more to guess the number. This repeats the process three times untill the
    user is asked to enter a DIFFERENT number.
    '''

    count = 0
    while True:
        if count < 2:
            if question() == True:
                print("Good job!")
                break
            else:                
                print("Try agian")
                count = count + 1
        elif count == 2:
            if question() == True:
                print("Good job!")
                break
            else:
                print ("Whoops! Try guessing a different number! ")

# Prints the title screen

title()

# Asks the user for their name

name = str(input("What is your name?: "))

# Greets the user using their name and explains the game

print("Hello!", name, "and welcome to the number game!")
print("in this game you will guess a number from one to five, there will be five rounds.")
print("Good Luck!")

askquestion()
print("Good job! Time for round 2!")
askquestion()
print("Good job! Time for round 3!")
askquestion()
print("Good job! Time for round 4!")
askquestion()
print("Good job! Time for round 5!")
askquestion()
print("Good job! You have beaten the numbers game.")