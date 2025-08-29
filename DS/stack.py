class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=node("head")
        self.size=0

    def getsize(self):
        return self.size
    
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    
    def push(self,value):
        temp=node(value)
        temp.next=self.head.next
        self.head.next=temp
        self.size+=1

    def pop(self):
        if self.head.next is None:
            print("Stack is empty")
            return None
        popped = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        print(popped.value)

    def peek(self):
        return self.head.next.value
    

s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print("peek without pop=",s1.peek())
print("POP ELEMENT= ",end="")
s1.pop()
print("peek after pop=",s1.peek())