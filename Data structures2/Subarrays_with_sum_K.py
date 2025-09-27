class Solution:
    def cntSubarrays(self, arr, k):
        prefix_sum = 0
        count = 0
        freq = {0: 1}  # base case: prefix sum 0 exists once

        for num in arr:
            prefix_sum += num
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
if __name__ == "__main__":
    sol = Solution()

    print(sol.cntSubarrays([10, 2, -2, -20, 10], -10))  # Expected 3
    print(sol.cntSubarrays([9, 4, 20, 3, 10, 5], 33))   # Expected 2
    print(sol.cntSubarrays([1, 3, 5], 0))               # Expected 0
    print(sol.cntSubarrays([1, 2, 3], 3))               # Expected 2 ([1,2], [3])
    print(sol.cntSubarrays([5, -5, 5, -5, 5], 5))       # Expected 6
