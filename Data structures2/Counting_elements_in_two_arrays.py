from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        """
        For each element in a, count elements in b less than or equal to it using sorting and binary search.
        """
        b.sort()  # Sort b for efficient counting
        return [bisect_right(b, x) for x in a]  # Count elements <= x using binary search

# Test cases
sol = Solution()

# Example 1
a1 = [4, 8, 7, 5, 1]
b1 = [4, 48, 3, 0, 1, 1, 5]
print(sol.countLessEq(a1, b1))  # Output: [5, 6, 6, 6, 3]

# Example 2
a2 = [10, 20]
b2 = [30, 40, 50]
print(sol.countLessEq(a2, b2))  # Output: [0, 0]

# Additional Test Case
a3 = [2, 5, 9]
b3 = [1, 2, 3, 4, 5]
print(sol.countLessEq(a3, b3))  # Output: [2, 5, 5]
