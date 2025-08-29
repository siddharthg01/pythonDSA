class Node:
    def __init__(nanu, value):
        nanu.val=value
        nanu.next=None

class SinglyLL:
    head=None

    def insertattail(nanu,value):
        if nanu.head==None:
            nanu.head=Node(value)
            return
        temp=nanu.head
        while temp.next!=None:
            temp=temp.next

        temp.next=Node(value)

    def insertAtstart(nanu,value):
        temp=Node(value)
        temp.next=nanu.head
        nanu.head=temp

    def insertanywhere(nanu,value,pos):
        if pos==1:
            nanu.insertAtstart(value)
            return
        temp=nanu.head

        count=2
        while count<pos and temp!=None:
            count+=1
            temp=temp.next

        if count<pos:
            print("The position overloaded")
            return
        past=temp.next
        temp.next=Node(value)
        temp.next.next=past

    def printlist(nanu):
        temp=nanu.head
        while temp!=None:
            print(temp.val,end=" ")
            temp=temp.next
    
    def delete(nanu, pos):
        if pos==1:
            nanu.head=nanu.head.next
            return
        count=2
        temp=nanu.head
        while count<pos and temp!=None:
            count+=1
            temp=temp.next

        if count<pos:
            print("Position overloaded")
            return
        
        temp.next=temp.next.next



ll=SinglyLL()
ll2=SinglyLL()
print("Insert at start:")
ll.insertAtstart(10)
ll.insertAtstart(20)
ll.insertAtstart(30)
ll.printlist()


print("\nInsert at end:")
ll2.insertattail(10)
ll2.insertattail(20)
ll2.insertattail(30)
ll2.printlist()


print("\nInsert Anywhere")
pos=int(input("Enter the position u want to insert:"))
val=int(input("Enter the value u would like to insert:"))
ll2.insertanywhere(val,pos)
ll2.printlist()

print("\nDeletion")
pos=int(input("Enter the position where u have to delete the value:"))
ll2.delete(pos)
ll2.printlist()