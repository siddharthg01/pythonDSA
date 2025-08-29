class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    head=None

    def insertattail(self,value):
        if self.head==None:
            self.head=Node(value)
            return
        
        temp=self.head

        while temp.next!=None:
            temp=temp.next

        temp.next=Node(value)

    def insertAtbegi(self,value):

        if self.head==None:
            self.head=Node(value)
            return
        
        temp=self.head
        self.head=Node(value)
        self.head.next=temp


    def insertAnywhere(self, value, position):
        if position==1:
            self.insertAtbegi(value)
            return
        
        temp=self.head
        count=2
        while count<position and temp!=None:
            count+=1
            temp=temp.next

        past=temp.next
        temp.next=Node(value)
        temp.next.next=past

    def print(self):
        temp=self.head

        while temp!=None:
            print(temp.value, end="-->")
            temp=temp.next

    def reverse(self):
        prev=None
        next1=None
        curr=self.head

        while curr!=None:
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1

        self.head=prev

ll1=LinkedList()
def switch_example(value):
    match value:
        case 1:
            val=int(input("Enter the value to insert at beginning:"))
            ll1.insertAtbegi(val)
        case 2:
            val=int(input("Enter the value to insert at end: "))
            ll1.insertattail(val)
        case 3:
            pos=int(input("Enter the position where you have to insert value:"))
            val=int(input("Enter the value to insert: "))
            ll1.insertAnywhere(val,pos)

        case 4:
            ll1.reverse()
        case 5:
            ll1.print()

m=0

while m!=6:
    print("\n--- Singly Linked List Menu ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at anywhere")
    print("4. Enter 4 for reversing the linked list")
    print("5. Display list")
    print("6. Exit")
    m=int(input("Enter your choice: "))
    switch_example(m)

    
