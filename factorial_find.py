def factorial(num):
    if num < 0:
        return 'the factorial of negative number is not possible'
    elif num == 0:
        return 'the factorial is 1'
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
num= int(input('Entre the number to find factorial of'))
fact = factorial(num)
print(f"The factorial of {num} is {fact}")