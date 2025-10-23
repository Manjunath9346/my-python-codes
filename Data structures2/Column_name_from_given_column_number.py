class Solution:
    def colName(self, n):
        result = ""
        while n > 0:
            n -= 1  # Adjust for 1-indexed alphabet (A=1,...,Z=26)
            result = chr(n % 26 + ord('A')) + result
            n //= 26
        return result
sol = Solution()

# Test case 1
print(sol.colName(28))   #  AB

# Test case 2
print(sol.colName(13))   #  M

# Test case 3
print(sol.colName(5473578))  #  KYJZF

# Test case 4
print(sol.colName(1))    #  A

# Test case 5
print(sol.colName(26))   #  Z

# Test case 6
print(sol.colName(52))   #  AZ

# Test case 7
print(sol.colName(703))  #  AAA
