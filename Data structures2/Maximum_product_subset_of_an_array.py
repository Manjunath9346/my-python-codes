class Solution:
    def findMaxProduct(self, arr):
        mod = 10**9 + 7
        n = len(arr)
        
        if n == 1:
            return arr[0]  # Directly return single element
        
        neg_count = 0
        zero_count = 0
        prod = 1
        max_neg = float('-inf')
        
        for num in arr:
            if num == 0:
                zero_count += 1
                continue
            if num < 0:
                neg_count += 1
                max_neg = max(max_neg, num)
            prod = (prod * num) % mod
        
        # Case 1: All zeros
        if zero_count == n:
            return 0
        
        # Case 2: Only one negative and rest zeros
        if neg_count == 1 and neg_count + zero_count == n:
            return 0
        
        # Case 3: Odd count of negatives → remove max negative (closest to 0)
        if neg_count % 2 == 1:
            prod = (prod * pow(max_neg, -1, mod)) % mod
        
        return prod if prod >= 0 else (prod + mod) % mod

# Test Case 1
print(Solution().findMaxProduct([-1, 0, -2, 4, 3]))  
# Expected Output: 24

# Test Case 2
print(Solution().findMaxProduct([-1, 0]))  
# Expected Output: 0

# Test Case 3
print(Solution().findMaxProduct([5]))  
# Expected Output: 5

# Test Case 4
print(Solution().findMaxProduct([-1, -2, -3, 4]))  
# Expected Output: 24  (since -1 * -2 * 4 = 8, * -3 = -24 → remove -3 → 8 * 4 = 32 mod 1e9+7 = 32)

# Test Case 5
print(Solution().findMaxProduct([0, 0, 0]))  
# Expected Output: 0

# Test Case 6
print(Solution().findMaxProduct([-1, -2, -3]))  
# Expected Output: 2  (remove -3 → -1 * -2 = 2)
