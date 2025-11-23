from collections import deque

class Solution:
    def max_of_subarrays(self, arr, n, k):
        dq = deque()     # will store indices of useful elements
        result = []

        for i in range(n):

            # remove elements out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # maintain decreasing order in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # window starts producing output after first k-1 elements
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
N = 9
K = 3
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]

Expected Output:
[3, 3, 4, 5, 5, 5, 6]
