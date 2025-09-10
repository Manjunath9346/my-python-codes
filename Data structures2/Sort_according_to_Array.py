class Solution:
    def relativeSort(self, a1, a2):
        # Build order map with first occurrence only
        order = {}
        pos = 0
        for num in a2:
            if num not in order:   # keep first occurrence only
                order[num] = pos
                pos += 1

        # Custom sort
        a1.sort(key=lambda x: (order.get(x, len(order)), x))
        return a1
sol = Solution()

print(sol.relativeSort([2, 1, 2, 3, 4], [2, 1, 2]))
# Output: [2, 2, 1, 3, 4]

print(sol.relativeSort([4, 1, 3, 3, 2], [3, 1]))
# Output: [3, 3, 1, 2, 4]

print(sol.relativeSort([7, 5, 9, 5, 8], [5, 7]))
# Output: [5, 5, 7, 8, 9]

print(sol.relativeSort([10, 20, 30], [40, 50]))
# Output: [10, 20, 30]

# 🔥 Your failing case:
print(sol.relativeSort([9, 5, 2, 6, 10, 6, 8, 9, 5, 4], [3, 5, 3, 2, 5, 5, 8]))
# Correct Output: [5, 5, 2, 8, 4, 6, 6, 9, 9, 10]
