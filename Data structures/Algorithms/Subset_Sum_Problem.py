class Solution:
    def isSubsetSum(self, arr, sum):
        n = len(arr)
        
        # Create a DP table with dimensions (n+1) x (sum+1)
        dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

        # A sum of 0 is always possible (with empty subset)
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the subset table
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  # Exclude current element
                else:
                    # Include or exclude the current element
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        return dp[n][sum]

s = Solution()

# Test case 1
arr1 = [3, 34, 4, 12, 5, 2]
sum1 = 9
print(s.isSubsetSum(arr1, sum1))  # Expected: True (e.g., 4+3+2)

# Test case 2
arr2 = [3, 34, 4, 12, 5, 2]
sum2 = 30
print(s.isSubsetSum(arr2, sum2))  # Expected: False
