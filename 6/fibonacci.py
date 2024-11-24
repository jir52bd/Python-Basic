#input the number
number = int(input("Enter the number "))

fib1 = 1
fib2 = 1
i = 0
print(fib1)
print(fib2)
while i < (number - 2):
    i += 1
    fib = fib1+fib2
    fib1 = fib2
    fib2 = fib
    print(fib)
