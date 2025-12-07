class Solution:
    def getMinMax(self, arr):
        mn = float('inf')
        mx = float('-inf')

        for num in arr:
            if num < mn:
                mn = num
            if num > mx:
                mx = num

        return [mn, mx]
obj = Solution()

print(obj.getMinMax([1, 4, 3, -5, -4, 8, 6]))
# Expected: [-5, 8]

print(obj.getMinMax([12, 3, 15, 7, 9]))
# Expected: [3, 15]

print(obj.getMinMax([5]))
# Expected: [5, 5]

print(obj.getMinMax([-10, -20, -3]))
# Expected: [-20, -3]
