class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = arr[:]  # Initialize dp with the same values as arr

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])

        return max(dp)
sol = Solution()

# Test Case 1
arr = [1, 101, 2, 3, 100]
print(sol.maxSumIS(arr))  # Output: 106

# Test Case 2
arr = [4, 1, 2, 3]
print(sol.maxSumIS(arr))  # Output: 6

# Test Case 3
arr = [4, 1, 2, 4]
print(sol.maxSumIS(arr))  # Output: 7

# Test Case 4 (Single element)
arr = [10]
print(sol.maxSumIS(arr))  # Output: 10
