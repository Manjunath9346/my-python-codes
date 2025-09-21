class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isDeadEnd(self, root):
        """
        Check whether BST contains a dead end using recursion with min-max value tracking.
        """
        def helper(node, low, high):
            if not node:
                return False
            # Dead end occurs if no number can be placed in [low, high]
            if low == high:
                return True
            return (helper(node.left, low, node.data - 1) or
                    helper(node.right, node.data + 1, high))

        return helper(root, 1, float('inf'))

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

root1 = buildTree([8, 5, 9, 2, 7, None, None, 1])
print(sol.isDeadEnd(root1))  # Output: True

root2 = buildTree([8, 7, 10, 2, None, 9, 13])
print(sol.isDeadEnd(root2))  # Output: True

root3 = buildTree([5, 2, 8])  
print(sol.isDeadEnd(root3))  # Output: False
