#define a class
class Bike:
    name=''
    gear = 0

#create object of a class
bike1 = Bike()
bike2 = Bike()

#accdess attributes and assingn the new values
bike1.name = "Mountain Bike"
bike1.gear = 11

print(f"Name :{bike1.name} and Gear :{bike1.gear}")

#access bike2
bike2.name = "Hero Bike"
bike2.gear = 13
print(f"Name :{bike2.name} and Gear :{bike2.gear}")
