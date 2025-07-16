from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        def compare(x, y):
            return -1 if x + y > y + x else 1

        # Convert all numbers to strings
        arr = list(map(str, arr))
        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        # Join the result
        result = ''.join(arr)
        # Handle case where all numbers are 0
        return '0' if result[0] == '0' else result
sol = Solution()
print(sol.findLargest([3, 30, 34, 5, 9]))     # Output: "9534330"
print(sol.findLargest([54, 546, 548, 60]))    # Output: "6054854654"
print(sol.findLargest([3, 4, 6, 5, 9]))       # Output: "96543"
