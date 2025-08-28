class Solution:
    def nthRoot(self, n, m):
        if m == 0:
            return 0
        if m == 1:
            return 1
        
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            power = mid ** n
            
            if power == m:
                return mid
            elif power < m:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
sol = Solution()

print(sol.nthRoot(3, 27))   # 3  (3^3 = 27)
print(sol.nthRoot(3, 9))    # -1 (no integer root)
print(sol.nthRoot(4, 625))  # 5  (5^4 = 625)
print(sol.nthRoot(2, 16))   # 4  (4^2 = 16)
print(sol.nthRoot(5, 32))   # 2  (2^5 = 32)
print(sol.nthRoot(2, 20))   # -1 (sqrt(20) not integer)
print(sol.nthRoot(10, 1))   # 1  (1^10 = 1)
print(sol.nthRoot(3, 0))    # 0  (0^3 = 0)
