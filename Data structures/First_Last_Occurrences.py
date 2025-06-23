class Solution:
    def find(self, arr, x):
        n = len(arr)
        
        def first_occurrence():
            low, high, res = 0, n - 1, -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        def last_occurrence():
            low, high, res = 0, n - 1, -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        first = first_occurrence()
        last = last_occurrence()
        return [first, last]
sol = Solution()

print(sol.find([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))   # Output: [2, 5]
print(sol.find([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))   # Output: [6, 6]
print(sol.find([1, 2, 3], 4))                        # Output: [-1, -1]
print(sol.find([5, 5, 5, 5, 5], 5))                  # Output: [0, 4]
print(sol.find([1, 2, 3, 4, 5], 1))                  # Output: [0, 0]
