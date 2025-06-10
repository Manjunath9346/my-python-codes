from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        if not arr or k == 0:
            return []
        
        dq = deque()
        result = []

        for i in range(n):
            # Remove elements out of this window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements (they will not be needed)
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            # Append result starting from i = k - 1
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
sol = Solution()
print(sol.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
# Output: [3, 3, 4, 5, 5, 5, 6]
