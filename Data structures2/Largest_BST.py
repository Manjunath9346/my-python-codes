class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def largestBst(self, root):
        self.max_bst_size = 0

        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))  # is_bst, size, min, max

            l_is_bst, l_size, l_min, l_max = dfs(node.left)
            r_is_bst, r_size, r_min, r_max = dfs(node.right)

            if l_is_bst and r_is_bst and l_max < node.data < r_min:
                total_size = l_size + r_size + 1
                self.max_bst_size = max(self.max_bst_size, total_size)
                return (True, total_size, min(l_min, node.data), max(r_max, node.data))
            else:
                return (False, max(l_size, r_size), 0, 0)

        dfs(root)
        return self.max_bst_size
root = Node(5)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
