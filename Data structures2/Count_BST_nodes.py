class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getCount(self, root, l, h):
        """
        Count nodes in BST whose values lie in range [l, h] using recursion and BST property.
        """
        if not root:
            return 0
        # If current node is less than l, ignore left subtree
        if root.data < l:
            return self.getCount(root.right, l, h)
        # If current node is greater than h, ignore right subtree
        if root.data > h:
            return self.getCount(root.left, l, h)
        # Current node is in range, count it and recurse both sides
        return 1 + self.getCount(root.left, l, h) + self.getCount(root.right, l, h)

# Helper to build BST from level order input
def buildTree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = Node(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases
sol = Solution()

root1 = buildTree([10, 5, 50, 1, None, 40, 100])
print(sol.getCount(root1, 5, 45))  # Output: 3
print(sol.getCount(root1, 10, 100))  # Output: 4

root2 = buildTree([1, 2, 3])
print(sol.getCount(root2, 23, 95))  # Output: 0
