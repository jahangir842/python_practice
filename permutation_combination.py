def factorial(num):
    # Base case: factorial of 0 is 1
    if num == 0:
        print('base case call')
        return 1

    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        num = num * factorial(num - 1)
        print('Recursive case call')
    return(num)
# Permutaion Calculation

def per_calc(n, r):
    perm = factorial(n) / factorial(n - r)
    return perm
def comb_calc(n, r):
    comb = factorial(n) / (factorial(r) * factorial(n -r))
    return comb
n = 9
r = 3
print(per_calc(n, r))
print(comb_calc(n, r))
# num= 5
# fact = factorial(num)
# print(f"The factorial of {num} is {fact}")