class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        if k <= 1:
            return 0
        prod = 1
        left = 0
        count = 0
        
        for right in range(n):
            prod *= arr[right]
            
            while prod >= k:
                prod //= arr[left]
                left += 1
            
            count += (right - left + 1)
        
        return count
# Test case 1
print(Solution().countSubArrayProductLessThanK([1, 2, 3, 4], 4, 10))  
# Expected: 7

# Test case 2
print(Solution().countSubArrayProductLessThanK([1, 9, 2, 8, 6, 4, 3], 7, 100))  
# Expected: 16

# Test case 3 (edge case: k = 1)
print(Solution().countSubArrayProductLessThanK([1, 2, 3], 3, 1))  
# Expected: 0

# Test case 4
print(Solution().countSubArrayProductLessThanK([10, 5, 2, 6], 4, 100))  
# Expected: 8
