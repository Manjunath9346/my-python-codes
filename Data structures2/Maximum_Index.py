class Solution:
    def maxIndexDiff(self, arr):
        n = len(arr)
        
        # Step 1: Create left_min[] and right_max[] arrays
        left_min = [0] * n
        right_max = [0] * n

        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(arr[i], left_min[i-1])

        right_max[n-1] = arr[n-1]
        for j in range(n-2, -1, -1):
            right_max[j] = max(arr[j], right_max[j+1])

        # Step 2: Traverse using two pointers
        i = j = 0
        max_diff = 0
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1

        return max_diff
sol = Solution()
print(sol.maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1]))  # Output: 6
print(sol.maxIndexDiff([18, 17]))                         # Output: 0
print(sol.maxIndexDiff([10, 10, 10, 10]))                 # Output: 3
