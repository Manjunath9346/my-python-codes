
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addnode(root, data):
    newnode = Node(data)
    if root == None:
        root = newnode
    else:
        if data < root.data:
            root.left = addnode(root.left, data)
        else:
            root.right = addnode(root.right, data)
    return root



def preorder(root):
    if root == None:
        return
    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)



def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

def postorder(root):
    if root == None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = " ")




def breadthfirsttraversal(root):
    queue = []
    queue.insert(0, root)
    while len(queue) != 0:
        curr = queue.pop()
        print(curr.data)
        if curr.left != None:
            queue.insert(0, curr.left)
        if curr.right != None:
            queue.insert(0, curr.right)
    return

def depthfirsttraversal(root):
    stack = []
    stack.append(root)
    while len(stack) != 0:
        curr= stack.pop()
        print(curr.data)
        if curr.right != None:
            stack.append( curr.right)
        if curr.left != None:
            stack.append(curr.left)
    return



root = None
root = addnode(root,  50)
addnode(root, 40)
addnode(root, 60)
addnode(root, 35)
addnode(root, 45)
addnode(root, 55)
addnode(root, 65)
preorder(root)
print()
inorder(root)
print()
postorder(root)
breadthfirsttraversal(root)
depthfirsttraversal(root)
