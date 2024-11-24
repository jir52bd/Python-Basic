# #input the valu of the number
# number = float(input("Enter the number : "))
#
# #input the power of the numeber
# power = int(input("Enter the power : "))
#
# y = 1.0
# i = 0
# while i < power:
#     y = y*number
#     i = i+1
#
# print(y)

def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    else:
        result = x
        for _ in range(n-1):
            result *=x
    return result


#Read the input
x = float(input("Enter the value of the  number : "))
n = int(input("Enter the power of the number : "))

#Call function
y = power(x, n)

print(f"{x}^{n} =", y)