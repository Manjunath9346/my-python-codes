class Solution:
    def kthFromLeaf(self, root, k):
        self.count = 0
        visited = set()  # to ensure unique nodes only

        def dfs(node, path):
            if not node:
                return
            path.append(node)
            
            # If it's a leaf node
            if not node.left and not node.right:
                if len(path) - k - 1 >= 0:
                    ancestor = path[-k-1]
                    visited.add(ancestor)
            
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return len(visited)
# Helper class to build tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Example 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(Solution().kthFromLeaf(root, 2))  # ✅ Output: 2

# Example 2
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(60)

print(Solution().kthFromLeaf(root, 1))  # ✅ Output: 2
