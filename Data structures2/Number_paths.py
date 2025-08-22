import math

class Solution:
    def numberOfPaths(self, m, n):
        # Using nCr formula
        return math.comb(m+n-2, m-1)
obj = Solution()
print(obj.numberOfPaths(3, 3))  # 6
print(obj.numberOfPaths(2, 3))  # 3
print(obj.numberOfPaths(1, 4))  # 1
print(obj.numberOfPaths(5, 5))  # 70
