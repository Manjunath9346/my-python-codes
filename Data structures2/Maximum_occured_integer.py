class Solution:
    def maxOccured(self, L, R):
        # Step 1: Find max value in R to size our array
        max_val = max(R)
        arr = [0] * (max_val + 2)

        # Step 2: Range updates
        for i in range(len(L)):
            arr[L[i]] += 1
            arr[R[i] + 1] -= 1

        # Step 3: Prefix sum to find frequencies
        max_count = arr[0]
        res = 0
        for i in range(1, max_val + 1):
            arr[i] += arr[i - 1]
            if arr[i] > max_count:
                max_count = arr[i]
                res = i
        return res
sol = Solution()

# Example 1
print(sol.maxOccured([1, 4, 3, 1], [15, 8, 5, 4]))
# Expected: 4

# Example 2
print(sol.maxOccured([1, 5, 9, 13, 21], [15, 8, 12, 20, 30]))
# Expected: 5

# Edge Case: Single range
print(sol.maxOccured([5], [10]))
# Expected: 5 (only one range, starts at 5)

# Edge Case: Multiple overlaps
print(sol.maxOccured([2, 2, 2], [4, 4, 4]))
# Expected: 2 (heaviest overlap at 2)

# Edge Case: Disjoint ranges
print(sol.maxOccured([1, 10, 20], [5, 15, 25]))
# Expected: 1 (smallest integer with max occurrence = 1)
