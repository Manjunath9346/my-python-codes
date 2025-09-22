# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def diagonal(self, root):
        """
        Perform diagonal traversal using queue by pushing left children
        and traversing right pointers.
        """
        if not root:
            return []
        
        result, q = [], [root]
        
        while q:
            node = q.pop(0)
            while node:
                result.append(node.data)
                if node.left:
                    q.append(node.left)
                node = node.right
        
        return result

# Helper to build tree from level order input
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

# Example 1
root1 = buildTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
print(sol.diagonal(root1))  # Output: [8, 10, 14, 3, 6, 7, 13, 1, 4]

# Example 2
root2 = buildTree([1, 2, None, 3, None])
print(sol.diagonal(root2))  # Output: [1, 2, 3]

# Additional Test
root3 = buildTree([5, 3, 8, 1, 4, 7, 9])
print(sol.diagonal(root3))  # Possible Output: [5, 8, 9, 3, 4, 7, 1]
