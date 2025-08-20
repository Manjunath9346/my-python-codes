from typing import List

class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # Step 1: LIS (Longest Increasing Subsequence) for each index
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Step 2: LDS (Longest Decreasing Subsequence) for each index
        lds = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Step 3: Find max(LIS[i] + LDS[i] - 1), ensuring bitonic
        max_len = 0
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:  # must have both inc and dec part
                max_len = max(max_len, lis[i] + lds[i] - 1)
        
        return max_len

# Example usage:
sol = Solution()
print(sol.LongestBitonicSequence(5, [1, 2, 5, 3, 2]))        # Output: 5
print(sol.LongestBitonicSequence(8, [1, 11, 2, 10, 4, 5, 2, 1])) # Output: 6
print(sol.LongestBitonicSequence(3, [10, 20, 30]))           # Output: 0
print(sol.LongestBitonicSequence(3, [10, 10, 10]))           # Output: 0
