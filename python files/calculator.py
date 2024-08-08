from multiprocessing import Value


start = int(input('Welcome to Geno\'s calculator V2! Please enter \"1\" to proceed: '))
if start == 1:
    valuecount = int(input('Great! How many values will you use in your equation? (2 or 3): '))

#prompts the user to input an operation and two values

    if valuecount == 2:
        value1 = int(input('Superb! Please enter your first value: '))
        operation = int(input('Now enter the ID of which operation you wish to use! (1-Addition, 2-Subtraction, 3-Multiplication, 4-Division): '))
        value2 = int(input('Almost done! Please enter your last value: '))

#calculates and prints the equation the user has built

        if operation == 1:
            print(value1,' + ',value2,' = ',value1+value2)
        elif operation == 2:
            print(value1,' - ',value2,' = ',value1-value2)
        elif operation == 3:
            print(value1,' x ',value2,' = ',value1*value2)
        else:
            if Value != 0:
                print(value1,' / ',value2,' = ',value1/value2)
            else:
                print('Error: Division by zero is not allowed')

#prompts the user to input two operations and three values

    else:
        value1 = int(input('Superb! Please enter your first value: '))
        operation1 = int(input('Now enter the ID of which operation you wish to use first! (1-Addition, 2-Subtraction, 3-Multiplication, 4-Division): '))
        value2 = int(input('Now please enter your second value: '))
        operation2 = int(input('Now enter the ID of which operation you wish to use second! (1-Addition, 2-Subtraction, 3-Multiplication, 4-Division): '))
        value3 = int(input('Almost done! Please enter your final value: '))

#calculates and prints the equation the user has built

        if operation1 == 1:
            if operation2 == 1:
                print(value1,' + ',value2,' + ',value3,' = ',value1+value2+value3)
            elif operation2 == 2:
                print(value1,' + ',value2,' - ',value3,' = ',value1+value2-value3)
            elif operation2 == 3:
                print(value1,' + ',value2,' x ',value3,' = ',value1+value2*value3)
            else:
                if value3 != 0:
                    print(value1,' + ',value2,' / ',value3,' = ',value1+value2/value3)
                else:
                    print('Error: Division by zero is not allowed')

        elif operation1 == 2:
            if operation2 == 1:
                print(value1,' - ',value2,' + ',value3,' = ',value1-value2+value3)
            elif operation2 == 2:
                print(value1,' - ',value2,' - ',value3,' = ',value1-value2-value3)
            elif operation2 == 3:
                print(value1,' - ',value2,' x ',value3,' = ',value1-value2*value3)
            else:
                if value3 != 0:
                    print(value1,' - ',value2,' / ',value3,' = ',value1-value2/value3)
                else:
                    print('Error: Division by zero is not allowed')
        elif operation1 == 3:
            if operation2 == 1:
                print(value1,' x ',value2,' + ',value3,' = ',value1*value2+value3)
            elif operation2 == 2:
                print(value1,' x ',value2,' - ',value3,' = ',value1*value2-value3)
            elif operation2 == 3:
                print(value1,' x ',value2,' x ',value3,' = ',value1*value2*value3)
            else:
                if value3 != 0:
                    print(value1,' x ',value2,' / ',value3,' = ',value1*value2/value3)
                else:
                    print('Error: Division by zero is not allowed')
        else:
            if value2 != 0:
                if operation2 == 1:
                    print(value1,' / ',value2,' + ',value3,' = ',value1/value2+value3)
                elif operation2 == 2:
                    print(value1,' / ',value2,' - ',value3,' = ',value1/value2-value3)
                elif operation2 == 3:
                    print(value1,' / ',value2,' x ',value3,' = ',value1/value2*value3)
                else:
                    print(value1,' / ',value2,' / ',value3,' = ',value1/value2/value3)
            else:
                print('Error: Division by zero is not allowed')

#prints a goodbye message if the user does not type "1" to begin

else:
    print('Goodbye!')