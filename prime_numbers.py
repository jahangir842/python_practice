def prime_calculate(num):
    for i in range(2, num):
        if (num % i)==0: 
            print(num)      
            return False
            break
        else:
            return True


num = 9

# num = int(input("enter the number to calculate prime number"))
Prime = prime_calculate(num)
if (Prime):
    print(f"{num} is Prime Number")
else:
    print(f'{num} is not Prime Number')