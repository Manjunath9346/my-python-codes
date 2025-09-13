class Solution:
    # Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root):
        self.max_sum = float('-inf')   # global maximum

        def dfs(node):
            if not node:
                return 0
            # Compute maximum path sum from left and right child
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Update global max: node as root of the path
            self.max_sum = max(self.max_sum, node.data + left + right)

            # Return max gain if parent continues path via this node
            return node.data + max(left, right)

        dfs(root)
        return self.max_sum
# Helper function to build tree manually
root1 = Node(10)
root1.left = Node(2)
root1.right = Node(10)
root1.left.left = Node(20)
root1.left.right = Node(1)
root1.right.right = Node(-25)
root1.right.right.left = Node(3)
root1.right.right.right = Node(4)

print(Solution().findMaxSum(root1))  # Output: 42

root2 = Node(-17)
root2.left = Node(11)
root2.right = Node(4)
root2.left.left = Node(20)
root2.left.right = Node(-2)
root2.right.left = Node(10)

print(Solution().findMaxSum(root2))  # Output: 31
