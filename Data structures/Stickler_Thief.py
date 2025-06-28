class Solution:  
    def findMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])
        
        dp = [0]*n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        
        return dp[-1]
sol = Solution()

# Test Case 1
print(sol.findMaxSum([6, 5, 5, 7, 4]))  # Output: 15

# Test Case 2
print(sol.findMaxSum([1, 5, 3]))        # Output: 5

# Test Case 3
print(sol.findMaxSum([4, 4, 4, 4]))     # Output: 8

# Test Case 4
print(sol.findMaxSum([10]))            # Output: 10

# Test Case 5
print(sol.findMaxSum([5, 1, 1, 5]))     # Output: 10
