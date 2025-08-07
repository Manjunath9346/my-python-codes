class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def deleteNode(root, X):
    if not root:
        return None

    if X < root.data:
        root.left = deleteNode(root.left, X)
    elif X > root.data:
        root.right = deleteNode(root.right, X)
    else:
        # Node to be deleted found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children: Get inorder successor (smallest in the right subtree)
        succ = root.right
        while succ.left:
            succ = succ.left

        root.data = succ.data  # Replace with successor value
        root.right = deleteNode(root.right, succ.data)  # Delete successor

    return root

# Helper function to do inorder traversal
def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []
# Tree: [1, None, 2, None, 8, 5, 11, 4, 7, 9, 12], Delete x = 11

root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(8)
root3.right.right.left = Node(5)
root3.right.right.right = Node(11)
root3.right.right.left.left = Node(4)
root3.right.right.left.right = Node(7)
root3.right.right.right.left = Node(9)
root3.right.right.right.right = Node(12)

new_root3 = deleteNode(root3, 11)
print("Inorder after deleting 11:", inorder(new_root3))  # Output: [1, 2, 4, 5, 7, 8, 9, 12]
