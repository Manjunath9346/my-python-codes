class Solution:
    def sumOfLongRootToLeafPath(self, root):
        def dfs(node):
            if not node: return (0, 0)  # (length, sum)
            l_len, l_sum = dfs(node.left)
            r_len, r_sum = dfs(node.right)

            if l_len > r_len:  # left path longer
                return (l_len + 1, l_sum + node.data)
            elif r_len > l_len:  # right path longer
                return (r_len + 1, r_sum + node.data)
            else:  # equal length, take max sum
                return (l_len + 1, max(l_sum, r_sum) + node.data)

        return dfs(root)[1]
# Example 1
# Tree: [4, 2, 5, 7, 1, 2, 3, N, N, 6, N]
# Longest path: 4 -> 2 -> 1 -> 6 = 13
print(Solution().sumOfLongRootToLeafPath(root1))  # 13

# Example 2
# Tree: [1, 2, 3, 4, 5, 6, 7]
# Longest path: 1 -> 3 -> 7 = 11
print(Solution().sumOfLongRootToLeafPath(root2))  # 11

# Example 3
# Tree: [10, 5, 15, 3, 7, N, 20, 1]
# Longest path: 10 -> 5 -> 3 -> 1 = 19
print(Solution().sumOfLongRootToLeafPath(root3))  # 19
