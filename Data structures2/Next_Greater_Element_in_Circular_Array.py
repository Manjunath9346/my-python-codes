class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []  # will store indices
        
        # Traverse the array twice to simulate circularity
        for i in range(2 * n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i % n]:
                stack.pop()
            if stack:
                res[i % n] = arr[stack[-1]]
            stack.append(i % n)
        
        return res
sol = Solution()

print(sol.nextGreater([1, 3, 2, 4]))     # [3, 4, 4, -1]
print(sol.nextGreater([0, 2, 3, 1, 1]))  # [2, 3, -1, 2, 2]
print(sol.nextGreater([5, 4, 3, 2, 1]))  # [-1, 5, 5, 5, 5]
print(sol.nextGreater([2, 2, 2]))        # [-1, -1, -1]
print(sol.nextGreater([10]))             # [-1]
