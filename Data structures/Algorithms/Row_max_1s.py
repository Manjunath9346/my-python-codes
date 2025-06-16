class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        max_row_index = -1
        j = m - 1  # Start from top-right corner

        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                max_row_index = i
                j -= 1  # Move left

        return max_row_index
arr = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

sol = Solution()
print(sol.rowWithMax1s(arr))  # Output: 2
