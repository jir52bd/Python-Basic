#Python Program to Add Two Numbers

def add_fun(n1, n2):
    return n1+n2


#Input two number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add_result = add_fun(num1, num2)

print(f"{num1} + {num2} = ", add_result)