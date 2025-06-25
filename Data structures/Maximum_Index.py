class Solution:
    def maxIndexDiff(self, arr):
        n = len(arr)
        right_max = [0] * n
        right_max[-1] = arr[-1]
        
        for i in range(n-2, -1, -1):
            right_max[i] = max(arr[i], right_max[i+1])
        
        max_diff = 0
        i = j = 0
        
        while i < n and j < n:
            if arr[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1
        
        return max_diff
arr = [249, 280, 19, 372, 118, 692, 405, 799, 487, 157, 382, 604, 677, 991, 735, 251, 958, 597, 990, 256, 755]
print(Solution().maxIndexDiff(arr))  # Should return 673 for full array
