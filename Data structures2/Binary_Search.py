class Solution:
    def binarysearch(self, arr, k):
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                result = mid            # store the index
                high = mid - 1          # move left to find first occurrence
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return result
obj = Solution()

print(obj.binarysearch([1, 2, 3, 4, 5], 4))          # Expected: 3
print(obj.binarysearch([11, 22, 33, 44, 55], 445))    # Expected: -1
print(obj.binarysearch([1, 1, 1, 1, 2], 1))           # Expected: 0
print(obj.binarysearch([5], 5))                       # Expected: 0
print(obj.binarysearch([2, 4, 6, 8, 10], 6))          # Expected: 2
print(obj.binarysearch([1, 2, 2, 2, 3], 2))           # Expected: 1
