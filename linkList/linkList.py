
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")




#Create a link list
llist = LinkList()

#appending element to the next node
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)

#display the linklist
llist.display()