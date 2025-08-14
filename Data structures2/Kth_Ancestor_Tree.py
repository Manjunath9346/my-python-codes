class Solution:
    def kthAncestor(self, root, k, node):
        path = []

        def dfs(cur):
            if not cur:
                return False
            path.append(cur.data)
            if cur.data == node:
                return True
            if dfs(cur.left) or dfs(cur.right):
                return True
            path.pop()
            return False

        dfs(root)
        return path[-k-1] if len(path) > k else -1
# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.right = Node(6)

# Create solution instance
sol = Solution()

# Test cases
print(sol.kthAncestor(root, 1, 7))  # Expected 5 (parent of 7)
print(sol.kthAncestor(root, 2, 7))  # Expected 2 (grandparent of 7)
print(sol.kthAncestor(root, 3, 7))  # Expected 1 (great-grandparent of 7)
print(sol.kthAncestor(root, 4, 7))  # Expected -1 (does not exist)
print(sol.kthAncestor(root, 1, 4))  # Expected 2 (parent of 4)
print(sol.kthAncestor(root, 2, 6))  # Expected 1 (grandparent of 6)
