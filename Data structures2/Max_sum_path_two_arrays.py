class Solution:
    def maxPathSum(self, arr1, arr2):
        i = j = 0
        s1 = s2 = res = 0
        n, m = len(arr1), len(arr2)
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            elif arr2[j] < arr1[i]:
                s2 += arr2[j]
                j += 1
            else:  # Common element
                res += max(s1, s2) + arr1[i]
                s1 = s2 = 0
                i += 1
                j += 1
                
        # Add remaining elements
        res += max(s1 + sum(arr1[i:]), s2 + sum(arr2[j:]))
        return res
# Test Case 1
print(Solution().maxPathSum([2, 3, 7, 10, 12], [1, 5, 7, 8]))  
# Output: 35

# Test Case 2
print(Solution().maxPathSum([1, 2, 3], [3, 4, 5]))  
# Output: 15

# Test Case 3
print(Solution().maxPathSum([1, 4, 5, 6, 8], [2, 3, 4, 6, 9]))  
# Output: 29

# Test Case 4
print(Solution().maxPathSum([10, 12], [5, 7, 9]))  
# Output: 28

# Test Case 5
print(Solution().maxPathSum([1, 3, 5], [2, 4, 6]))  
# Output: 12
