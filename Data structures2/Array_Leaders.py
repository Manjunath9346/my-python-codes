class Solution:
    def leaders(self, arr):
        n = len(arr)
        max_right = arr[-1]
        result = [max_right]          # last element is always a leader

        # traverse from right to left
        for i in range(n-2, -1, -1):
            if arr[i] >= max_right:
                result.append(arr[i])
                max_right = arr[i]

        return result[::-1]           # reverse to restore original order
Input:
arr = [16, 17, 4, 3, 5, 2]
Output:
[17, 5, 2]
Input:
arr = [10, 4, 2, 4, 1]
Output:
[10, 4, 4, 1]
