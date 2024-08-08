functionname = int(input('Welcome to Geno\'s calculator, please select the fuction you would like to use (1=multiply, 2=add, 3=subract 4=divide): '))

if functionname == 1:
    valuecount = int(input('Multiplication! Please input how many values you wish to use (1, 2, or 3): '))
    if valuecount == 3:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        value3 = int(input('Please input your third value: '))
        print(value1,' x ',value2,' x ',value3,' = ', value1*value2*value3,'!')
    if valuecount == 2:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        print(value1,' x ',value2,' = ', value1*value2,'!')
    if valuecount == 1:
        value1 = int(input('Please input your first value: '))
        print(value1,' = ',value1,'!')

if functionname == 2:
    valuecount = int(input('Addition! Please input how many values you wish to use (1, 2, or 3): '))
    if valuecount == 3:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        value3 = int(input('Please input your third value: '))
        print(value1,' + ',value2,' + ',value3,' = ', value1+value2+value3,'!')
    if valuecount == 2:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        print(value1,' + ',value2,' = ',value1+value2,'!')
    if valuecount == 1:
        value1 = int(input('Please input your first value: '))
        print(value1,' = ',value1,'!')

if functionname == 3:
    valuecount = int(input('Subraction! Please input how many values you wish to use (1, 2, or 3): '))
    if valuecount == 3:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        value3 = int(input('Please input your third value: '))
        print(value1,' - ',value2,' - ',value3,' = ', value1-value2-value3,'!')
    if valuecount == 2:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        print(value1,' - ',value2,' = ', value1-value2,'!')
    if valuecount == 1:
        value1 = int(input('Please input your first value: '))
        print(value1,' = ',value1,'!')

if functionname == 4:
    valuecount = int(input('Division! Please input how many values you wish to use (1, 2, or 3): '))
    if valuecount == 3:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        value3 = int(input('Please input your third value: '))
        print(value1,' / ',value2,' / ',value3,' = ', value1/value2/value3,'!')
    if valuecount == 2:
        value1 = int(input('Please input your first value: '))
        value2 = int(input('Please input your second value: '))
        print(value1,' / ',value2,' = ',value1/value2,'!')
    if valuecount == 1:
        value1 = int(input('Please input your first value: '))
        print(value1,' = ',value1,'!')
