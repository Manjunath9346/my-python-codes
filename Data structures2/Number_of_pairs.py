from bisect import bisect_right

class Solution:
    # Function to count number of pairs such that x^y > y^x
    def countPairs(self, arr, brr):
        # Sort second array
        brr.sort()
        n = len(brr)
        
        # Count special cases for small numbers
        count_y = [0] * 5
        for y in brr:
            if y < 5:
                count_y[y] += 1
        
        ans = 0
        for x in arr:
            if x == 1:
                continue  # 1^y is never > y^1 (except y=1 which is equal)
            
            # Count how many y > x
            idx = bisect_right(brr, x)
            ans += n - idx  # all y > x contribute
            
            # Add special cases
            ans += count_y[1]  # x^1 > 1^x for all x > 1
            
            if x == 2:
                ans -= (count_y[3] + count_y[4])  # exceptions
            if x == 3:
                ans += count_y[2]  # 3^2 > 2^3
                
        return ans
sol = Solution()

# Example 1
print(sol.countPairs([2, 1, 6], [1, 5]))  
# Expected: 3 (pairs: (2,1), (2,5), (6,1))

# Example 2
print(sol.countPairs([2, 3, 4, 5], [1, 2, 3]))  
# Expected: 5 (pairs: (2,1), (3,1), (3,2), (4,1), (5,1))

# Edge Case 1
print(sol.countPairs([1,1,1], [1,1,1]))  
# Expected: 0 (all 1^1 = 1)

# Edge Case 2
print(sol.countPairs([10], [2,3,4]))  
# Expected: 3 (10^y > y^10 for y=2,3,4)

# Large values
print(sol.countPairs([1000], [1,2,3,4,1000]))  
# Expected: 4
