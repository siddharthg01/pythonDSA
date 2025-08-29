class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

class Stack:
    def __init__(self):
        self.head= Node("dummy")
        self.size=0

    def isEmpty(self):
        if self.size==0:
            return True
        return False
    def push(self, value):
        temp=Node(value)
        temp.next= self.head.next
        self.head.next = temp
        self.size+=1        

    def pop(self):
        if self.isEmpty()==True:
            print("Stack is empty return")
            return
        
        popped= self.head.next

        self.head.next= self.head.next.next
        self.size-=1

        print("Popped: ",popped.value)
    
    def top(self):
        print("Top=",self.head.next.value)
        return
    def getsize(self):
        print("Size of stack is:",self.size)
        return
    
stack= Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.top()
stack.getsize()
stack.pop()

stack.top()

print(stack.isEmpty())
stack.getsize()