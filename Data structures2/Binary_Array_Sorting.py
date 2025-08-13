class Solution:
    def binSort(self, arr):
        zero_count = arr.count(0)
        for i in range(len(arr)):
            arr[i] = 0 if i < zero_count else 1
sol = Solution()

arr1 = [1, 0, 1, 1, 0]
sol.binSort(arr1)
print(arr1)  # [0, 0, 1, 1, 1]

arr2 = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
sol.binSort(arr2)
print(arr2)  # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

arr3 = [1, 1, 1, 1]
sol.binSort(arr3)
print(arr3)  # [1, 1, 1, 1]
