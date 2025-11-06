class Solution:
    def maxDiff(self, root):  # ✅ include self
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), float('-inf')  # (min_val, max_val, max_diff)
            
            if not node.left and not node.right:
                return node.data, node.data, float('-inf')
            
            lmin, lmax, ldiff = helper(node.left)
            rmin, rmax, rdiff = helper(node.right)
            
            min_child = min(lmin, rmin)
            max_child = max(lmax, rmax)
            
            # Calculate max diff for current node
            curr_diff = max(ldiff, rdiff, node.data - min_child)
            
            return min(node.data, min_child), max(node.data, max_child), curr_diff
        
        _, _, ans = helper(root)
        return ans
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Example 1
root = Node(5)
root.left = Node(2)
root.right = Node(1)

sol = Solution()
print(sol.maxDiff(root))  # ✅ Output: 4
