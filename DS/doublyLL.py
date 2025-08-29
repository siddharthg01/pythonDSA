class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:

    head=None

    def insertatBeginning(self, value):

        if self.head==None:
            self.head=Node(value)
            return

        temp=self.head
        self.head=Node(value)
        self.head.next=temp
        temp.prev=self.head


    def insertatend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insertatanywhere(self,value,pos):
        if pos == 1:
            self.insertatBeginning(value)
            return
        temp= self.head
        count = 1
        while temp is not None and count < pos-1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range.")
            return

        new_node = Node(value)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    def print(self):
        temp=self.head

        while temp!=None:
            print(temp.prev,"-->",temp.value,"-->",temp.next)
            temp=temp.next

ll1=LinkedList()

ll1.insertatend(50)
ll1.insertatend(40)
ll1.insertatend(30)
ll1.insertatend(20)
ll1.insertatend(10)
ll1.insertatanywhere(900000,2)
ll1.print()