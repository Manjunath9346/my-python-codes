from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        q = deque()
        res = []

        for i in range(n):
            # Add index of negative numbers
            if arr[i] < 0:
                q.append(i)
            
            # Remove elements out of this window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Start recording results once we have first full window
            if i >= k - 1:
                if q:
                    res.append(arr[q[0]])
                else:
                    res.append(0)
        return res
sol = Solution()

# Test Case 1
print(sol.firstNegInt([-8, 2, 3, -6, 10], 2))  
# Output: [-8, 0, -6, -6]

# Test Case 2
print(sol.firstNegInt([12, -1, -7, 8, -15, 30, 16, 28], 3))  
# Output: [-1, -1, -7, -15, -15, 0]

# Test Case 3
print(sol.firstNegInt([12, 1, 3, 5], 3))  
# Output: [0, 0]

# Test Case 4
print(sol.firstNegInt([-5, -10, 0, 3, 2], 1))  
# Output: [-5, -10, 0, 3, 2]
