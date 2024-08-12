import random

def intinput(message):
    try:
        userinput = int(input(message))
    except ValueError:
        pass
    return userinput
    

def genadd(range):
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


roundcount = 0
while True:
    if roundcount < 4:
        genadd(100)
        print("Good job! Time for round", roundcount + 2, "!")
        print()
        roundcount = roundcount + 1
    else:
        genadd(100)
        break

print()
print("Now time for subtraction!")
print()

roundcount = 0
while True:
    if roundcount < 4:
        gensub(100)
        print("Good job! Time for round", roundcount + 2, "!")
        print()
        roundcount = roundcount + 1
    else:
        gensub(100)
        break

print("-------------------------------------------")
print()
print("Congrats! You have beaten the numbers game.")
print("          (press enter to close)           ")
print()
print("-------------------------------------------")

input()
