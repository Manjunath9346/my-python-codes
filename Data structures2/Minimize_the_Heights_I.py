# User function Template for python3

class Solution:
    def getMinDiff(self, arr, k):
        if not arr or len(arr) == 1:
            return 0
        
        arr.sort()  # Sort to handle smallest and largest easily
        n = len(arr)
        ans = arr[-1] - arr[0]  # Initial difference without modification
        
        for i in range(1, n):
            high = max(arr[i-1] + k, arr[-1] - k)  # Max after modification
            low = min(arr[0] + k, arr[i] - k)      # Min after modification
            ans = min(ans, high - low)             # Update minimum difference
        
        return ans

# Example usage:
sol = Solution()
print(sol.getMinDiff([1, 5, 8, 10], 2))        # Output: 5
print(sol.getMinDiff([3, 9, 12, 16, 20], 3))   # Output: 11
