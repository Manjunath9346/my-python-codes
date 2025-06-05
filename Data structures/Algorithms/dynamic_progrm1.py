# User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        mod = 10**9 + 7
        n = len(arr)
        
        # Initialize a 2D dp array with (n+1) x (target+1)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        
        # Base Case: There's always one subset (empty set) for sum = 0
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j - arr[i-1]]) % mod
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]
sol = Solution()
print(sol.perfectSum([5, 2, 3, 10, 6, 8], 10))  # Output: 3
print(sol.perfectSum([2, 5, 1, 4, 3], 10))      # Output: 3
print(sol.perfectSum([5, 7, 8], 3))             # Output: 0
print(sol.perfectSum([35, 2, 8, 22], 0))        # Output: 1
