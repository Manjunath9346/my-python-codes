class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0]*n for _ in range(n)]

        # Fill diagonal (when only one coin is left)
        for i in range(n):
            dp[i][i] = arr[i]

        # Solve for all subarray lengths
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                # Player chooses left or right, opponent also plays optimally
                left = arr[i] + min(dp[i+2][j] if i+2 <= j else 0,
                                    dp[i+1][j-1] if i+1 <= j-1 else 0)
                right = arr[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0,
                                     dp[i][j-2] if i <= j-2 else 0)
                dp[i][j] = max(left, right)

        return dp[0][n-1]
s = Solution()

print(s.maximumAmount([5, 3, 7, 10]))   # Expected 15
print(s.maximumAmount([8, 15, 3, 7]))   # Expected 22
print(s.maximumAmount([2, 2, 2, 2]))    # Expected 4
print(s.maximumAmount([20, 30, 2, 2, 2, 10]))  # Expected 42
print(s.maximumAmount([1, 100, 1]))     # Expected 100
