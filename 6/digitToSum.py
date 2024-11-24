

def digit_sum(n):
    sum = 0
    while n > 0:
        last_digit = n%10
        sum = sum+last_digit
        n = n // 10
    return sum


#input number
number = int(input("Enter the number: "))

#call the function to sum the digits
digits_sum = digit_sum(number)

#print digits sum
print(digits_sum)