from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Compute difference and keep original indices
        diff = [(abs(arr[i] - brr[i]), i) for i in range(n)]
        # Sort orders by descending absolute difference
        diff.sort(reverse=True)
        
        tip = 0
        a_count, b_count = 0, 0
        
        for d, i in diff:
            # Prefer person with higher tip for this order
            if (arr[i] >= brr[i] and a_count < x) or b_count == y:
                tip += arr[i]
                a_count += 1
            else:
                tip += brr[i]
                b_count += 1
        
        return tip
sol = Solution()

# Test 1
print(sol.maxTip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
# Output: 21

# Test 2
print(sol.maxTip(8, 4, 4, [1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8]))
# Output: 43

# Test 3
print(sol.maxTip(7, 3, 4, [8, 7, 15, 19, 16, 16, 18], [1, 7, 15, 11, 12, 31, 9]))
# Output: 110
