def multiply(num1, num2):
    ans = num1 * num2
    return ans

def factorial(number):
    for num in range(1, int(number)):
        number = multiply(number, num)
    return number
        
        

print(factorial(100))