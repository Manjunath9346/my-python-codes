class Solution:
    def longestSubarrayDivK(self, arr, k):
        prefix_sum = 0
        remainder_index = {0: -1}  # remainder -> first index
        max_len = 0

        for i, num in enumerate(arr):
            prefix_sum += num
            rem = prefix_sum % k

            # Handle negative remainders
            if rem < 0:
                rem += k

            if rem in remainder_index:
                max_len = max(max_len, i - remainder_index[rem])
            else:
                remainder_index[rem] = i

        return max_len
print(Solution().longestSubarrayDivK([2, 7, 6, 1, 4, 5], 3))
# Output: 4  (subarray [7,6,1,4])

print(Solution().longestSubarrayDivK([-2, 2, -5, 12, -11, -1, 7], 3))
# Output: 5  (subarray [2,-5,12,-11,-1])

print(Solution().longestSubarrayDivK([1, 2, -2], 2))
# Output: 2  (subarray [2,-2])

print(Solution().longestSubarrayDivK([5, 10, 15], 5))
# Output: 3  (whole array is divisible)
