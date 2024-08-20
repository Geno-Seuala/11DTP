import random


def intinput(message):
    """ Prevents crashing when inputting invalid inputs (e.g. inputting
    'abc' as an answer to 5 + 13. If the users input is invalid, 
    the program shows an error message and asks for another input 

    Arguments: message (the message to prompt the user to input a
    number

    Returns: an integer inputted by the user) """
    while True:
        try:
            userinput = int(input(message))
            break
        except ValueError:
            print()
            print("Please only input whole numbers")
            print()
    return userinput


def genadd(range):
    """ Generates and asks a random addition problem.

    Arguments: range (how big a number in the problem can be)

    Returns: a random addition problem
    """

    num1 = random.randint(1, range)
    num2 = random.randint(1, range)

    answer = num1+num2

# Checks if the answer is right and moves on if it is so that the next
# Question can be asked

    while True:
        if intinput(f"What is {num1} + {num2}?: ") == answer:
            print()
            print()
            break
        else:
            print()
            print("Whoops! Your answer is wrong, please try again.")
            print()


def gensub(range):
    """ Generates and asks a random subtraction problem with two numbers
    and ensures that the answer is a positive integer. 

    Arguments: range (how big a number in the problem can be)

    Returns: a random subtraction problem with a positive integer as the
    answer
    """

    num1 = random.randint(1, range)
    num2 = random.randint(1, range)

# This makes sure that the smaller number is subtracted from the larger
# Number to ensure that the answer is a positive integer
    if num1 > num2:
        answer = num1-num2
        question = f"What is {num1} - {num2}?: "
    elif num1 < num2:
        answer = num2-num1
        question = f"What is {num2} - {num1}?: "

# Checks if the answer is right and moves on if it is so that the next
# Question can be asked
    while True:
        if intinput(question) == answer:
            print()
            print()
            break
        else:
            print()
            print("Whoops! Your answer is wrong, please try again.")
            print()


# Prints a title screen to welcome the user and indicate that the
# Program has started and is running okay
print("---------------------------------------")
print()
print("      Welcome to the number game!      ")
print("           What is your name?          ")
print()
print("---------------------------------------")

# Asks the user for their name and ensures that it only contains letters
# This makes sure that the user inputs an actual name and not numbers
# Or symbols
while True:
    name = input('Please input a username: ')
    if any(char.isalpha() for char in name) == False:
        print("Invalid name! please use letters.")
        print("")
    else:
        break

# Greets the user by game and briefly explains the rules of the game so
# That the user know how to play and understands the game
print("------------------------------------------------------")
print()
print(f"    Hello! {name}! and welcome to the number game!   ")
print()
print("   you will solve addition and subtraction problems,  ")
print()
print("        After you guess the number correctly,         ")
print("   a new problem will be generated for you to solve   ")
print("               5 addition - 5 subtraction             ")
print()
print()
print("                     Good Luck!                       ")
print()
print("------------------------------------------------------")


# Generates and asks 5 random addition problems with values 1 - 100 so
# That the user can practice their number skills with addition
roundcount = 0
while roundcount < 4:
    genadd(100)
    print(f"Good job! Time for round {roundcount + 2}!")
    print()
    roundcount = roundcount + 1
print()

print("""Now time for subtraction!
""")

# Generates and asks 5 random subtraction problems with values 1 - 100
# So that the user can practice their number skills with subtraction
roundcount = 0
while roundcount < 4:
    gensub(100)
    print(f"Good job! Time for round {roundcount + 2}!")
    print()
    roundcount = roundcount + 1
print()

# Prints an end screen to tell to user that the game has finished
print("-------------------------------------------")
print()
print("Congrats! You have beaten the numbers game.")
print("          (press enter to close)           ")
print()
print("-------------------------------------------")

# Keeps the program running at the end so that the user can read the
# End screen    
input()
