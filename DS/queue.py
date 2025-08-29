class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head= Node("dummy")
        self.tail=self.head
        self.size=0

    def getsize(self):
        return self.size
    
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    
    def enqueue(self, value):

        self.tail.next= Node(value)
        self.tail= self.tail.next
        self.size+=1
        

    def dequeue(self):
        if self.isEmpty()==True:
            print("Queue is Empty")
            return
        removed= self.head.next
        self.size-=1
        self.head.next= self.head.next.next
        print("Removed front:",removed.value)
        print("Next front is:", self.head.next.value)
        

    def front(self):
        if self.isEmpty()==True:
            print("Queue is Empty")
            return
        return self.head.next.value



q= Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.front())

q.dequeue()
print(q.front())


