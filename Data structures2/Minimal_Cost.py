class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0  # cost to start at stone 0 is 0

        for i in range(1, n):
            for j in range(1, k + 1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))

        return dp[-1]
sol = Solution()

print(sol.minimizeCost(3, [10, 30, 40, 50, 20]))  # 30
print(sol.minimizeCost(1, [10, 20, 10]))          # 20
print(sol.minimizeCost(2, [10, 40, 30, 10]))      # 20
print(sol.minimizeCost(3, [5, 7, 3, 9, 2]))       # 7
print(sol.minimizeCost(4, [1, 2, 3, 4, 5]))       # 4
