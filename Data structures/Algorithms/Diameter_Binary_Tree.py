# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def diameter(self, root):
        self.ans = 0

        def height(node):
            if not node:
                return 0
            # Recursively get height of left and right subtrees
            lh = height(node.left)
            rh = height(node.right)

            # Update diameter at this node
            self.ans = max(self.ans, lh + rh)
            
            # Return height of current node
            return 1 + max(lh, rh)

        height(root)
        return self.ans

# Test Case 1: Tree with three nodes
root1 = build_tree([1, 2, 3])
print(sol.diameter(root1))  # Expected: 2 (2 -> 1 -> 3)

# Test Case 2: More complex tree
root2 = build_tree([5, 8, 6, 3, 7, 9])
print(sol.diameter(root2))  # Expected: 4 (3 -> 8 -> 5 -> 6 -> 9)

# Test Case 3: Single node
root3 = build_tree([1])
print(sol.diameter(root3))  # Expected: 0 (no edges)

# Test Case 4: Left skewed tree
root4 = build_tree([1, 2, None, 3, None, 4])
print(sol.diameter(root4))
