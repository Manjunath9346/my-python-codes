class Solution:
    def isLucky(self, n):
        def check(num, i):
            if i > num:
                return True
            if num % i == 0:
                return False
            # Adjust position after removing every i-th number
            return check(num - num // i, i + 1)
        
        return 1 if check(n, 2) else 0
print(Solution().isLucky(5))   # Output: 0
print(Solution().isLucky(19))  # Output: 1
