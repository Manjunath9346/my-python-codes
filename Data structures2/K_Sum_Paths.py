class Solution:
    def sumK(self, root, k):
        from collections import defaultdict
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.data
            count = prefix[curr_sum - k]  # paths ending here with sum k
            
            prefix[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1  # backtrack
            
            return count
        
        prefix = defaultdict(int)
        prefix[0] = 1  # base case for paths starting at root
        return dfs(root, 0)
# Tree from example 1
def buildTree1():
    root = Node(8)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(2)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.right = Node(1)
    return root

root1 = buildTree1()
sol = Solution()
print(sol.sumK(root1, 7))  # Output: 3

# Tree from example 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
print(sol.sumK(root2, 3))  # Output: 2
