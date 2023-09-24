def factorial(num):
    # Base case: factorial of 0 is 1
    if num == 0:
        return 1

    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        num = num * factorial(num - 1)
    return(num)

num= 7
fact = factorial(num)
print(f"The factorial of {num} is {fact}")