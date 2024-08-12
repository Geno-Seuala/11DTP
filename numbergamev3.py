import random


def intinput(message):
    """ Prevents crashing when inputting invalid inputs (e.g. inputting
    'esgh' as an answer to 5 + 13. """
    try:
        userinput = int(input(message))
    except ValueError:
        pass
    return userinput


def genadd(range):
    """ Generates and asks a random addition problem with numbers from
    1 - 100. """
    num1 = random.randint(1, range)
    num2 = random.randint(1, range)

    answer = num1+num2

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
    from 1 - 100 and ensures that the answer is a positive integer. """

    num1 = random.randint(1, range)
    num2 = random.randint(1, range)

    if num1 > num2:
        answer = num1-num2
        question = f"What is {num1} - {num2}?: "
    elif num1 < num2:
        answer = num2-num1
        question = f"What is {num2} - {num1}?: "

    while True:
        if intinput(question) == answer:
            print()
            print()
            break
        else:
            print()
            print("Whoops! Your answer is wrong, please try again.")
            print()


print("---------------------------------------")
print()
print("      Welcome to the number game!      ")
print("           What is your name?          ")
print()
print("---------------------------------------")

# Asks the user for their name and ensures that it only contains letters
while True:
    name = input('Please input a username: ')
    if any(char.isalpha() for char in name) == False:
        print("Invalid name! please use letters.")
        print("")
    else:
        break

# Greets the user and briefly explains the rules of the game
print("------------------------------------------------------")
print()
print("   Hello!", name, "! and welcome to the number game!  ")
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


# Generates and asks 5 random addition problems with values 1 - 100
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
roundcount = 0
while roundcount < 4:
    gensub(100)
    print(f"Good job! Time for round {roundcount + 2}!")
    print()
    roundcount = roundcount + 1
print()

# Prints an end screen
print("-------------------------------------------")
print()
print("Congrats! You have beaten the numbers game.")
print("          (press enter to close)           ")
print()
print("-------------------------------------------")

input()
