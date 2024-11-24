# Solve the quadratic equation ax**2 + bx + c = 0
import cmath as cm
def quadratic_equation(a, b, c):
    #calculate the discrimination
    discrimination = b*b - 4*a*c
    print(discrimination)
    #check the value of discrimination
    if discrimination > 0:
        root1 = -b+cm.sqrt(discrimination)/(2*a)
        root2 = -b-cm.sqrt(discrimination)/(2*a)
        return root1, root2
    elif discrimination == 0:
        root = -b/2*a
        return root, root #Repeated root
    else:
        real_part = -b/2*a
        imaginary_part = cm.sqrt(abs(discrimination))/(2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, imaginary_part)
        return root1, root2
#Get the Coefficient from the user
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))

root = quadratic_equation(a, b, c)
print("Root - ", root)