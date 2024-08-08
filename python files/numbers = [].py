numbers = []
for num in range(0, 10):
    number = int(input("Enter number: "))
    numbers.append(number)
odd = []
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Odds:', odd, "Evens:", even)