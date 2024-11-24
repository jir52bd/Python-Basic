
#creating a stack
def Stack():
    stack = []
    return stack
#checking stack
def check_empty(stack):
    return len(stack) == 0

#Addign item in the stack
def push(stack, item):
    stack.append(item)
    print(f"{item} is add  in the stack")

#Removing an item from the stack
def pop(stack):
    if check_empty(stack):
        return "Stack is empty"

    return stack.pop()

stack = Stack()
#Adding item
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))

print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))