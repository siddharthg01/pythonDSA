class Node:
    def __init__(nanu,value):
        nanu.val=value
        nanu.next=None

class LL:
    head=None

    def insertattail(nanu,value):
        if nanu.head==None:
            nanu.head=Node(value)
            return
        temp=nanu.head

        while temp.next!=None:
            temp=temp.next

        temp.next=Node(value)

    def returnMiddle(nanu):
        """ temp=nanu.head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next

        mid= count//2 +1
        temp1=nanu.head
        while mid!=1:
            temp1=temp1.next
            mid-=1

        print("\n",temp1.val) """
        fast=nanu.head
        slow=nanu.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        print("\n",slow.val)

        

    def printValues(nanu):
        temp=nanu.head

        while temp!=None:
            print(temp.val,end=" ")
            temp=temp.next

ll1=LL()

ll1.insertattail(1)
ll1.insertattail(2)
ll1.insertattail(3)
ll1.insertattail(4)
ll1.insertattail(5)
ll1.insertattail(6)
ll1.printValues()
ll1.returnMiddle()




