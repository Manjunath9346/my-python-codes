class Solution:
    def findTarget(self, root, target):
        # Helper to get next smallest element using inorder traversal
        def pushLeft(node):
            while node:
                stack1.append(node)
                node = node.left
        
        # Helper to get next largest element using reverse inorder traversal
        def pushRight(node):
            while node:
                stack2.append(node)
                node = node.right
        
        # Initialize two stacks for iterators
        stack1, stack2 = [], []
        pushLeft(root)
        pushRight(root)
        
        # Get next smallest value
        def nextSmall():
            node = stack1.pop()
            pushLeft(node.right)
            return node.data
        
        # Get next largest value
        def nextLarge():
            node = stack2.pop()
            pushRight(node.left)
            return node.data
        
        # Initialize smallest and largest
        left = nextSmall()
        right = nextLarge()
        
        # Two-pointer search directly on BST
        while left < right:
            s = left + right
            if s == target:
                return True
            elif s < target:
                left = nextSmall()
            else:
                right = nextLarge()
        return False

# Helper function to build tree quickly (for testing)
class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

# Test 1
root = Node(7)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)
print(Solution().findTarget(root, 12))  
#  Output: True (4 + 8 = 12)

# Test 2
root = Node(9)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(12)
print(Solution().findTarget(root, 23))  
#  Output: False
