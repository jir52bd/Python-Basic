
#Prime number check
def is_prime(n):
    #Basic case test
    if n <= 1:
        return False
    if n <= 3:
        return True
    #Trial divison
    if n % 2 == 0 or n % 3 == 0:
        return False
    #Optimozation

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

#Test case
number = int(input("Enter a integer number "))

#Call prime checker function
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")