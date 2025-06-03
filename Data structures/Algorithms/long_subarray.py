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
# Example usage
arr1 = [10, 5, 2, 7, 1, -10]
k1 = 15

arr2 = [-5, 8, -14, 2, 4, 12]
k2 = -5

arr3 = [10, -10, 20, 30]
k3 = 5

sol = Solution()
print("Longest Subarray Length:", sol.longestSubarray(arr1, k1))  # Output: 6
print("Longest Subarray Length:", sol.longestSubarray(arr2, k2))  # Output: 5
print("Longest Subarray Length:", sol.longestSubarray(arr3, k3))  # Output: 0
