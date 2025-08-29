class Node:
    def __init__(self,val):
        self.val=val
        self.next= None

class LL:
    head=None

    def insertAtTail(self,value):

        if self.head==None:
            self.head = Node(value)
            return
        
        temp= self.head

        while temp.next!=None:
            temp=temp.next

        temp.next= Node(value)

    def insertAtstart(self,value):
        temp = Node(value)
        temp.next= self.head
        self.head= temp

    def insertAtAnywhere(self,value,pos):
        if pos==1:
            self.insertAtstart(value)
            return
        
        temp=self.head

        count=2

        while count<pos and temp!=None:
            count+=1
            temp=temp.next

        if count<pos:
            print("Position overloaded")
            return
        
        past=temp.next
        temp.next=Node(value)
        temp.next.next=past

    def print(self):
        temp=self.head

        while temp!=None:
            print(temp.val,end=" ")
            temp=temp.next

    def delete(self,pos):

        if pos==1:
            self.head=self.head.next
            return
        
        temp=self.head

        count=2

        while count<pos and temp!=None:
            count+=1
            temp=temp.next
        

        if count<pos:
            print("Not a valid position")
            return
        temp.next= temp.next.next

ll = LL()

ll.insertAtTail(1)
ll.insertAtTail(2)
ll.insertAtTail(3)
ll.insertAtTail(4)
ll.insertAtTail(5)
ll.print()
pos=int(input("\nEnter the position where u want to insert in the above prebuilt list:"))
value=int(input(f"Enter some value to insert in {pos}:"))
ll.insertAtAnywhere(value,pos)
ll.print()


print("\n\t")

ll.insertAtstart(900)
print("Insertion at beginning is taking place........")
ll.print()

