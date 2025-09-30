
class Solution:
    def getMaxSum(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (include, exclude)
            
            left_incl, left_excl = dfs(node.left)
            right_incl, right_excl = dfs(node.right)
            
            # If we include this node, we cannot include its children
            include = node.data + left_excl + right_excl
            
            # If we exclude this node, we can choose max from children
            exclude = max(left_incl, left_excl) + max(right_incl, right_excl)
            
            return (include, exclude)
        
        incl, excl = dfs(root)
        return max(incl, excl)

# Example 1
root = Node(11)
root.left = Node(1)
root.right = Node(2)
print(Solution().getMaxSum(root))  # Expected 11

# Example 2
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
print(Solution().getMaxSum(root))  # Expected 16

# Edge case: single node
root = Node(10)
print(Solution().getMaxSum(root))  # Expected 10

# Edge case: skewed tree
root = Node(5)
root.left = Node(10)
root.left.left = Node(20)
root.left.left.left = Node(1)
print(Solution().getMaxSum(root))  # Expected 25 (10 + 1 + 14)
