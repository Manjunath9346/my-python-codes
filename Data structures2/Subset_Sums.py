class Solution:
    def subsetSums(self, arr):
        res = []

        def helper(i, current_sum):
            if i == len(arr):
                res.append(current_sum)
                return
            # Include arr[i]
            helper(i + 1, current_sum + arr[i])
            # Exclude arr[i]
            helper(i + 1, current_sum)

        helper(0, 0)
        return res
# Test Case 1
arr = [2, 3]
print(Solution().subsetSums(arr))
# Expected Output (order can vary): [0, 3, 2, 5]

# Test Case 2
arr = [1, 2, 1]
print(Solution().subsetSums(arr))
# Expected Output (order can vary): [0, 1, 2, 3, 1, 2, 3, 4]

# Test Case 3
arr = [5, 6, 7]
print(Solution().subsetSums(arr))
# Expected Output (order can vary): [0, 5, 6, 7, 11, 12, 13, 18]

# Test Case 4 (Single element)
arr = [4]
print(Solution().subsetSums(arr))
# Expected Output: [0, 4]

# Test Case 5 (All zeros)
arr = [0, 0]
print(Solution().subsetSums(arr))
# Expected Output: [0, 0, 0, 0]
