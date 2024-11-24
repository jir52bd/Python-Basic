def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_euler_number(n):
    e = 0
    for i in range(n + 1):
        e += 1 / factorial(i)
    return e

# Read input
n = int(input("Enter the value of n: "))

# Calculate the value of Euler's number using the compute_euler_number function
euler_number = compute_euler_number(n)

# Print the calculated value of Euler's number
print("Euler's Number (e):", euler_number)
