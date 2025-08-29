class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class CLL:
    tail=None

    def insertatEnd(self, value):
        newNode=Node(value)
        if self.tail==None:
            self.tail=newNode
            self.tail.next=self.tail
            return
        else:
            newNode.next=self.tail.next
            self.tail.next=newNode
            self.tail=newNode

    def insertAtBeg(self,value):
        newNode=Node(value)

        if self.tail==None:
            self.tail=newNode
            self.tail.next=self.tail

        newNode.next=self.tail.next
        self.tail.next=newNode


    def insertAtanywhere(self,value,position):
        new_node = Node(value)
        if position < 1:
            print("Invalid position")
            return

        # Case 1: Insert at beginning
        if position == 1:
            if self.tail is None:
                self.tail = new_node
                self.tail.next = self.tail
            else:
                new_node.next = self.tail.next
                self.tail.next = new_node
            return

        # Case 2: Insert at middle or end using while loop
        curr = self.tail.next
        index = 1

        while index < position - 1 and curr.next != self.tail.next:
            curr = curr.next
            index += 1

        if index != position - 1:
            print("Position out of bounds")
            return

        new_node.next = curr.next
        curr.next = new_node

        if curr == self.tail:
            self.tail = new_node


    def print(self):
        if self.tail is None:
            print("List is empty")
            return

        curr = self.tail.next
        while True:
            print(curr.value, end=" -> ")
            curr = curr.next
            if curr == self.tail.next:
                break
        print("(back to head)")

ll2= CLL()

print("\nInsert at end:")
ll2.insertatEnd(10)
ll2.insertatEnd(20)
ll2.insertatEnd(30)
ll2.print()

print("\nInsert Anywhere")
pos=int(input("Enter the position u want to insert:"))
val=int(input("Enter the value u would like to insert:"))
ll2.insertAtanywhere(val,pos)
ll2.print()
    


