class Solution:
    def countWays(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
print(Solution().countWays(1))  # Output: 1
print(Solution().countWays(2))  # Output: 2
print(Solution().countWays(4))  # Output: 5
print(Solution().countWays(5))  # Output: 8
print(Solution().countWays(10)) # Output: 89
