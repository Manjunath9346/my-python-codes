class Solution:
    def findDuplicates(self, arr):
        n = len(arr)
        res = []

        for i in range(n):
            idx = abs(arr[i]) - 1   # convert value to index

            if arr[idx] < 0:
                res.append(abs(arr[i]))   # seen before → duplicate
            else:
                arr[idx] *= -1            # mark visited

        return res
Input:
arr = [2, 3, 1, 2, 3]
Output:
[2, 3]
Input:
arr = [4, 3, 2, 7, 8, 2, 3, 1]
Output:
[2, 3]
