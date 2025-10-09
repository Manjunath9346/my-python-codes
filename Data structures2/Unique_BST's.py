class Solution:
    # Function to return the total number of possible unique BSTs.
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty tree
        
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        
        return dp[n]
sol = Solution()

# Test 1
print(sol.numTrees(2))  # Output: 2

# Test 2
print(sol.numTrees(3))  # Output: 5

# Test 3
print(sol.numTrees(4))  # Output: 14

# Test 4
print(sol.numTrees(1))  # Output: 1
