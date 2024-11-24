
def switch(case, n1, n2):
    if case == 1:
        return n1+n2
    elif case == 2:
        if n1> n2:
            return n1 - n2
        else:
            return n2 - n1
    elif case == 3:
        return n1*n2
    else:
        if n1 > n2:
            return float(n1//n2)
        else:
            return float(n2//n1)

#enter two number
num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))

#slection information
print("Select operation ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

option = int(input("Enter the option 1/ 2/ 3/ 4 :"))

result = switch(option, num1, num2)

print(result)