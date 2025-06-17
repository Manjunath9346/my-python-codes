class Solution:
    def lis(self, arr):
        n = len(arr)
        dp = [1] * n  # Initialize LIS values for all indexes

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
arr = [5, 8, 3, 7, 9, 1]
sol = Solution()
print(sol.lis(arr))  # Output: 3
