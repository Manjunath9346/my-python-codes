# User function Template for python3

class Solution:
    def floor(self, root, x):
        ans = -1
        while root:
            if root.data == x:
                return x  # exact match
            elif root.data > x:
                root = root.left  # go left
            else:
                ans = root.data  # possible floor
                root = root.right  # go right to find larger but <= x
        return ans
# Helper function to build tree (for testing)
def build_bst():
    root = Node(2)
    root.right = Node(81)
    root.right.left = Node(42)
    root.right.right = Node(87)
    root.right.left.right = Node(66)
    root.right.left.right.left = Node(45)
    root.right.right.right = Node(90)
    return root

sol = Solution()

# Example 1
root1 = build_bst()
print(sol.floor(root1, 87))  # Output: 87

# Example 2
root2 = Node(6)
root2.right = Node(8)
root2.right.left = Node(7)
root2.right.right = Node(9)
print(sol.floor(root2, 11))  # Output: 9

# Example 3
root3 = Node(6)
root3.right = Node(8)
root3.right.left = Node(7)
root3.right.right = Node(9)
print(sol.floor(root3, 5))   # Output: -1
