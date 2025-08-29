if self.isEmpty()==True:
            self.tail.next= Node(value)
            self.head.next=self.tail.next
            self.size+=1