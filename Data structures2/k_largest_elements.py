import heapq

class Solution:
    def kLargest(self, arr, k):
        # Use nlargest from heapq for efficiency
        return heapq.nlargest(k, arr)
sol = Solution()

# Test Case 1
print(sol.kLargest([12, 5, 787, 1, 23], 2))  
# Output: [787, 23]

# Test Case 2
print(sol.kLargest([1, 23, 12, 9, 30, 2, 50], 3))  
# Output: [50, 30, 23]

# Test Case 3
print(sol.kLargest([12, 23], 1))  
# Output: [23]

# Test Case 4
print(sol.kLargest([4, 3, 5, 2, 1], 5))  
# Output: [5, 4, 3, 2, 1]
