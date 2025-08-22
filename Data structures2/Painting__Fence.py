class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return k * k

        same = k * 1       # ways when last 2 are same (for n=2)
        diff = k * (k-1)   # ways when last 2 are different (for n=2)

        for i in range(3, n+1):
            new_same = diff * 1
            new_diff = (same + diff) * (k-1)

            same, diff = new_same, new_diff

        return same + diff
obj = Solution()
print(obj.countWays(3, 2))  # Output: 6
print(obj.countWays(2, 4))  # Output: 16
print(obj.countWays(1, 5))  # Output: 5
print(obj.countWays(4, 3))  # Output: 66
