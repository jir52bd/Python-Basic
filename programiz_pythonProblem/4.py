#Python Program to Calculate the Area of a Triangle

def sort_three_number(a, b, c):
    if a <= b and a <= c:
        smallest = a
        if b <= c:
            middle = b
            largest = c
        else:
            middle = c
            largest = b
    elif b <= a and b <= c:
        smallest = b
        if a <= c:
            middle = a
            largest = c
        else:
            middle = c
            largest = a
    else:
        smallest = c
        if a <= b:
            middle = a
            largest = b
        else:
            middle = b
            largest = a

    return smallest, middle, largest

def area_triangle(n1, n2, n3):
    #sort three nuber
    a, b, c, = sort_three_number(n1, n2, n3)
    # print(a, b, c)
    if a+b <= c:
        raise ValueError("Triangle is not possible.")
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

#Inter the three arms of the trian23gle
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

area = area_triangle(a, b, c)

print(f"{a}, {b}, {c} the area of the values is %0.2f"%area)