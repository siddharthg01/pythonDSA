class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def preorder(currnode):
    if currnode==None:
        return

    print(currnode.data, end=" ")
    preorder(currnode.left)
    preorder(currnode.right)

def inorder(currnode):
    if currnode==None:
        return
    
    inorder(currnode.left)
    print(currnode.data,end=" ")
    inorder(currnode.right)

def postOrder(currnode):
    if currnode==None:
        return
    postOrder(currnode.left)
    postOrder(currnode.right)
    print(currnode.data,end=" ")

root = Node(1)
root.left= Node(2)
root.right =Node(3)

root.left.left=Node(4)
root.left.right = Node(5)

root.right.right= Node(6)
root.right.right.left = Node(7)

print("Preorder=")
preorder(root)
print("\nInorder=")
inorder(root)
print("\n Postorder=")
postOrder(root)