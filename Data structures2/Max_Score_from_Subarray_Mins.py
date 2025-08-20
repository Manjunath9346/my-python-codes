class Solution:
    def maxSum(self, arr):
        n = len(arr)
        max_score = 0
        
        # Check every adjacent pair
        for i in range(n - 1):
            max_score = max(max_score, arr[i] + arr[i + 1])
        
        return max_score

# Example usage:
sol = Solution()
print(sol.maxSum([4, 3, 5, 1]))  # Output: 8
print(sol.maxSum([1, 2, 3]))     # Output: 5
