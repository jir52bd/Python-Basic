
def area_triangle(a, b, c):
    s = (a+b+c)//2
    area = (s*(s-a)*s*(s-b)*s*(s-c))**.5
    return area

#Input for the three side of the triangle
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))

area = area_triangle(a, b, c)

print(area)
