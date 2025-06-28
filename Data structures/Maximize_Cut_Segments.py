class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        # Create a DP array initialized with -1
        dp = [-1] * (n + 1)
        dp[0] = 0  # No cuts needed to get length 0

        for i in range(1, n + 1):
            if i - x >= 0 and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i - y >= 0 and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i - z >= 0 and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)

        return max(dp[n], 0)
sol = Solution()

print(sol.maximizeTheCuts(4, 2, 1, 1))  # Output: 4
print(sol.maximizeTheCuts(5, 5, 3, 2))  # Output: 2
print(sol.maximizeTheCuts(7, 8, 9, 10)) # Output: 0
print(sol.maximizeTheCuts(9, 2, 2, 2))  # Output: 4
print(sol.maximizeTheCuts(11, 5, 3, 2)) # Output: 5
