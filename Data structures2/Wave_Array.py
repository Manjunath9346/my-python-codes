class Solution:
    def sortInWave(self, arr):
        n = len(arr)
        for i in range(0, n-1, 2):   # step = 2
            arr[i], arr[i+1] = arr[i+1], arr[i]
sol = Solution()

# Test case 1
arr1 = [1, 2, 3, 4, 5]
sol.sortInWave(arr1)
print(arr1)   # Output: [2, 1, 4, 3, 5]

# Test case 2
arr2 = [2, 4, 7, 8, 9, 10]
sol.sortInWave(arr2)
print(arr2)   # Output: [4, 2, 8, 7, 10, 9]

# Test case 3
arr3 = [1]
sol.sortInWave(arr3)
print(arr3)   # Output: [1]
