class Solution:
    def findSwapValues(self, a, b):
        sumA, sumB = sum(a), sum(b)
        diff = sumB - sumA
        if diff % 2 != 0:
            return False
        target = diff // 2
        setB = set(b)
        for x in a:
            if x + target in setB:
                return True
        return Falsesol = Solution()

print(sol.findSwapValues([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))  # True (swap 1 and 3)
print(sol.findSwapValues([5, 7, 4, 6], [1, 2, 3, 8]))        # True (swap 6 and 2)
print(sol.findSwapValues([3, 3], [6, 5, 6, 6]))              # False
print(sol.findSwapValues([1, 2, 3], [4, 5, 6]))              # False
print(sol.findSwapValues([10, 20], [30, 40]))                # False

