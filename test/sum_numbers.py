
def sum_numbers(n):
    sum = 0
    for i in range(1, num+1):
        sum +=i
    return sum

num = int(input("Enter a number "))

print(f"{sum_numbers(num)} is the sum of first  {num} numbers.")