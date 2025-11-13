class Solution:
    def countPairs(self, arr1, arr2):
        import bisect
        
        # Sort arr2
        arr2.sort()
        n = len(arr2)
        
        # Count occurrences of 0,1,2,3,4 in arr2 (special cases)
        count = [0] * 5
        for y in arr2:
            if y < 5:
                count[y] += 1

        def countForX(x):
            # If x == 0: no valid pair since 0^y < y^0 always
            if x == 0:
                return 0
            
            # If x == 1: only works with y = 0
            if x == 1:
                return count[0]

            # Find number of y such that y > x
            idx = bisect.bisect_right(arr2, x)
            ans = n - idx  # all y > x are valid generally
            
            # Add pairs with y = 0 or y = 1 (since x^0 = 1 and x^1 = x)
            ans += count[0] + count[1]

            # Special tricky cases:
            if x == 2:
                ans -= (count[3] + count[4])   # remove (2,3) and (2,4)
            if x == 3:
                ans += count[2]               # add (3,2)

            return ans
        
        total = 0
        for x in arr1:
            total += countForX(x)
        
        return total
sol = Solution()

print(sol.countPairs([2,1,6], [1,5]))
#  Expected: 3

print(sol.countPairs([10,19,18], [11,15,9]))
#  Expected: 2

print(sol.countPairs([1,2,3], [1,2,3]))
# Expected: (1,0)(2,1)(3,2) => 3

print(sol.countPairs([2,3], [3,4]))
# (2,3 false), (2,4 false), (3,3 false), (3,4 false) => 0

print(sol.countPairs([3], [2]))
# (3,2) true → 1
