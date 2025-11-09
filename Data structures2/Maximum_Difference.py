class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        left_smaller = [0] * n
        right_smaller = [0] * n
        stack = []

        # Find nearest smaller to the left
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            left_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])

        stack.clear()

        # Find nearest smaller to the right
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            right_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])

        # Calculate max absolute difference
        return max(abs(left_smaller[i] - right_smaller[i]) for i in range(n))
sol = Solution()

print(sol.findMaxDiff([2, 1, 8]))           #  Output: 1
print(sol.findMaxDiff([2, 4, 8, 7, 7, 9, 3]))  #  Output: 4
print(sol.findMaxDiff([1, 2, 3, 4]))        #  Output: 3
print(sol.findMaxDiff([4, 3, 2, 1]))        #  Output: 3
print(sol.findMaxDiff([5]))                 #  Output: 0
