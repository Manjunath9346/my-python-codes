class Solution:
    def searchInSorted(self, arr, k):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return False
obj = Solution()

print(obj.searchInSorted([1, 2, 3, 4, 6], 6))   # True
print(obj.searchInSorted([1, 2, 4, 5, 6], 3))   # False
print(obj.searchInSorted([2, 3, 5, 6], 1))      # False
print(obj.searchInSorted([10], 10))             # True
print(obj.searchInSorted([1, 3, 5, 7], 2))      # False
