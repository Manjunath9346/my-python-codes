class Solution:
    def longestSubarray(self, arr, k):
        sum_map = {}  # Stores (prefix_sum: first_index)
        max_len = 0
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]

            if curr_sum == k:
                max_len = i + 1  # From index 0 to i

            if (curr_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[curr_sum - k])

            if curr_sum not in sum_map:
                sum_map[curr_sum] = i  # Store first occurrence only

        return max_len
