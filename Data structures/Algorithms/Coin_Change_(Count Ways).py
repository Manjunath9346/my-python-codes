class Solution:
    def count(self, coins, sum):
        n = len(coins)
        dp = [0] * (sum + 1)
        dp[0] = 1  # There is 1 way to make sum 0 — no coins

        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] += dp[i - coin]

        return dp[sum]
sol = Solution()
print(sol.count([1, 2, 3], 4))  # Output: 4
print(sol.count([2, 5, 3, 6], 10))  # Output: 5
print(sol.count([5, 10], 3))  # Output: 0
