class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def isComplete(self, root, index, total_nodes):
        if not root:
            return True
        if index >= total_nodes:
            return False
        return (self.isComplete(root.left, 2 * index + 1, total_nodes) and
                self.isComplete(root.right, 2 * index + 2, total_nodes))
    
    def isHeapUtil(self, root):
        if not root.left and not root.right:
            return True
        if not root.right:
            return root.data >= root.left.data
        else:
            return (root.data >= root.left.data and
                    root.data >= root.right.data and
                    self.isHeapUtil(root.left) and
                    self.isHeapUtil(root.right))
    
    def isHeap(self, root):
        total_nodes = self.countNodes(root)
        return self.isComplete(root, 0, total_nodes) and self.isHeapUtil(root)
# Helper function to create the tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# First tree (Expected: True)
root1 = Node(97)
root1.left = Node(46)
root1.right = Node(37)
root1.left.left = Node(12)
root1.left.right = Node(3)
root1.right.left = Node(7)
root1.right.right = Node(31)
root1.left.left.left = Node(6)
root1.left.left.right = Node(9)

# Second tree (Expected: False)
root2 = Node(97)
root2.left = Node(46)
root2.right = Node(37)
root2.left.left = Node(12)
root2.left.right = Node(3)
root2.right.left = Node(7)
root2.right.right = Node(31)
root2.left.right.left = Node(2)
root2.left.right.right = Node(4)

# Testing
sol = Solution()
print(sol.isHeap(root1))  # True
print(sol.isHeap(root2))  # False
