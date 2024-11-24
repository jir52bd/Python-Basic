
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)




#crating an instance of Queue class
q = Queue()

q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)

q.display()

q.dequeue()
print("After dequeue the element :")
q.display()