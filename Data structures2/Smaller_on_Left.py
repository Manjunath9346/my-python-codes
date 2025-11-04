class Solution:
    def leftSmaller(self, arr):
        stack, result = [], []
        for num in arr:
            while stack and stack[-1] >= num:  # pop elements >= current
                stack.pop()
            result.append(stack[-1] if stack else -1)
            stack.append(num)
        return result
print(Solution().leftSmaller([1, 6, 2]))           # [-1, 1, 1]
print(Solution().leftSmaller([1, 5, 0, 3, 4, 5]))  # [-1, 1, -1, 0, 3, 4]
print(Solution().leftSmaller([4, 5, 2, 10, 8]))    # [-1, 4, -1, 2, 2]
print(Solution().leftSmaller([10, 20, 30]))        # [-1, 10, 20]
print(Solution().leftSmaller([5, 4, 3, 2, 1]))     # [-1, -1, -1, -1, -1]
