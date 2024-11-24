#Given a number, write a program using while loop to reverse the digits of the number.

def reverse_digits(n):
    reversed_number = 0
    while n > 0:
        last_digit = n%10
        reversed_number = reversed_number*10 + last_digit
        n = n // 10

    return reversed_number


#Read input
number = int(input("Enter a number: "))

#call the function to reverse the digit
reversed_number = reverse_digits(number)

#print the reverse number
print("Reverse number: ", reversed_number)