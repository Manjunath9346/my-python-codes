from collections import deque  # <-- ADD THIS LINE

class Solution:
    def Paths(self, root):
        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, path, result):
        if not node:
            return
        path.append(node.data)
        if not node.left and not node.right:
            result.append(path[:])
        else:
            self.dfs(node.left, path, result)
            self.dfs(node.right, path, result)
        path.pop()
# Helper Tree Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Helper function to build tree
def build_tree_from_list(lst):
    if not lst or lst[0] == 'N':
        return None
    nodes = [None if val == 'N' else Node(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Test Case 1
root = build_tree_from_list([1, 2, 3, 4, 5, 'N', 'N'])
print(Solution().Paths(root))
# Expected: [[1, 2, 4], [1, 2, 5], [1, 3]]

# Test Case 2
root = build_tree_from_list([1, 2, 3])
print(Solution().Paths(root))
# Expected: [[1, 2], [1, 3]]

# Test Case 3
root = build_tree_from_list([10, 20, 30, 40, 60, 'N', 'N'])
print(Solution().Paths(root))
# Expected: [[10, 20, 40], [10, 20, 60], [10, 30]]
