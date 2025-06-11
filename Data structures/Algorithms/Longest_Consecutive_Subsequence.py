class Solution:
    def longestConsecutive(self, arr):
        num_set = set(arr)
        max_length = 0

        for num in arr:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count how long the sequence continues
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                max_length = max(max_length, current_streak)

        return max_length
print(Solution().longestConsecutive([2, 6, 1, 9, 4, 5, 3]))     # Expected: 6 (1 to 6)
print(Solution().longestConsecutive([1, 9, 3, 10, 4, 20, 2]))   # Expected: 4 (1 to 4)
print(Solution().longestConsecutive([15, 13, 12, 14, 11, 10, 9]))  # Expected: 7 (9 to 15)
print(Solution().longestConsecutive([1, 1, 1, 1]))              # Expected: 1 (only one unique element)
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))    # Expected: 4 (1 to 4)
print(Solution().longestConsecutive([]))                       # Expected: 0 (empty array)
print(Solution().longestConsecutive([10]))                     # Expected: 1 (single element)
print(Solution().longestConsecutive([5, 6, 7, 8, 9]))           # Expected: 5 (all consecutive)
