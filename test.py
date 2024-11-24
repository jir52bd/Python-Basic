
# print("Hello world")
# x= 5
# y=4
# print(x+y)
#
# x = "awesome"
# global x
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)


a = 35e4
b = 4E4
c = -100.87e100
d = complex(a)
d = 2j #complex
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(d)

# random number
import random
print(random.randrange(1,10))

z = "Hello, python"
print(z[10])

for l in "Bangladesh":
  print("++\t"+l+"#")

tex = "This is my first cone in python"

print("cone" in tex)

if 'is' in tex:
  print("yes")

print("firs" not in tex)

hello = "Hello World"
print(hello[-9:-7])

print(hello.upper())
print(hello.lower())
print((hello.strip()))
print(hello.replace("e", "J"))
print(hello.split("H"))

good = "you are a "
worker = "good worker"
print(good+worker)

age = 36
tex = "Your age is {}"
print(tex.format(age))

quantity = 3
items = 456
price = 54.36
myorder = "I wll pay {2} dollars for {0} pieces item {1}"
print(myorder.format(quantity, items, price))

print(9 < 10)
print(9 == 10)
print(9 <= 10)

print(bool('hello'))
print(bool(15))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFun():
  return False

if myFun():
  print("Yes")
else:
  print("No")

p = 200
print(isinstance(p, int))

thisList = ['Apple', 'Banana', 'Orange']
print(thisList)
print(len(thisList))

if "Apple" in thisList:
  print("Yes, 'apple' is the fruit in the list")

thisList[1] = "Cherry"
print(thisList)

thisList.insert(1,"Banan")
print(thisList)

for x in range(len(thisList)):
  print(thisList[x])


  i = 0
  while i < len(thisList):
    print(thisList[i])
    i = i+1

fruits = ["Apple", "grapes", "Banana", "chery", "Dodo", "Orange"]
newList = []

for x in fruits:
  if "an" in x:
    newList.append(x)



print(newList)

fruits.sort()
print(fruits)


number = [100, 20, 30, 10, 50, 40]
number.sort(reverse=True)
print(number)

for i in fruits:
  number.append(i)

print(number)

thistupple = ("Razu", "Jahirul", "Islam")
print(thistupple)
print(type(thistupple))

thisdist = {
  "name": "Jahirul Islam Razu",
  "Relision": "Islam",
  "year":2023
}

print(thisdist["name"])

A = 20
B = 30
C = 40

if A > B and B > C:
  print("Both are True")

num = 12345
tem = num
revNum = 0
while(tem != 0):
  dig = tem%10
  tem = tem/10
  revNum = revNum*10 + dig

print("Original Number" + num)
print("Reverse Number" + revNum)


