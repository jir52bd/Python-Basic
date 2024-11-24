


#Number input
number = int(input("Enter a Number :"))

factorial_number = 1
#Call the function to multiplu the digit
if number > 0:
    while number > 0:
        factorial_number = factorial_number * number
        number = number-1

#print the factorial number
print("Factorial number ", factorial_number)