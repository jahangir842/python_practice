# Find PI to the Nth Digit - Enter a number and have the program generate p (pi)
# up to that many decimal places
# Keep a limit to how far the program will go.

# def find_py(num):
def calculate_pi(n):
    pi = 0.0
    for k in range(n):
        pi += ((-1) ** k) / (2 * k + 1)
    pi *= 4
    return pi

# Input the number of iterations (more iterations increase precision)
num_iterations = 6

# Calculate π
pi_value = calculate_pi(num_iterations)
print(f"π calculated to approximately {num_iterations} decimal places: {pi_value}")
