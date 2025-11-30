class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
obj = Solution()

print(obj.search([1, 2, 3, 4], 3))        # Expected: 2
print(obj.search([10, 8, 30, 4, 5], 5))   # Expected: 4
print(obj.search([10, 8, 30], 6))         # Expected: -1
print(obj.search([5, 5, 5], 5))           # Expected: 0
print(obj.search([], 3))                  # Expected: -1
