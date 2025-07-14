class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):  # rod length
            for j in range(1, i + 1):  # cut length
                dp[i] = max(dp[i], price[j - 1] + dp[i - j])
        
        return dp[n]
sol = Solution()
print(sol.cutRod([1, 5, 8, 9, 10, 17, 17, 20]))  # Output: 22
print(sol.cutRod([3, 5, 8, 9, 10, 17, 17, 20]))  # Output: 24
print(sol.cutRod([3]))                          # Output: 3
