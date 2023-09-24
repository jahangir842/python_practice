from decimal import Decimal, getcontext

def calculate_pi(n):
    # Set the precision (number of decimal places)
    getcontext().prec = n + 2  # We add 2 to ensure we have enough digits

    # Calculate π using the Chudnovsky algorithm
    pi = Decimal(0)
    k = 0
    for k in range(n + 1):
        pi += (Decimal(-1) ** k) * (Decimal(6 * k + 1) / (Decimal(3) ** k * Decimal(2 * k + 1)))

    return str(pi)[:-1]  # Return π as a string, removing the trailing 'L'

# Input the number of decimal places you want
num_decimal_places = 777

# Check for a reasonable limit (e.g., not too high to avoid very long calculations)
if num_decimal_places <= 1000:
    pi_value = calculate_pi(num_decimal_places)
    print(f"π to {num_decimal_places} decimal places: {pi_value}")
else:
    print("Please choose a lower number of decimal places for π.")

