class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        stack = []
        span = [0] * n

        for i in range(n):
            # Pop elements from stack while current price is higher
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()

            # If stack is empty, span is i+1
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push this element's index to stack
            stack.append(i)

        return span
ob = Solution()
print(ob.calculateSpan([100, 80, 60, 70, 60, 75, 85]))  # Output: [1, 1, 1, 2, 1, 4, 6]
print(ob.calculateSpan([10, 4, 5, 90, 120, 80]))        # Output: [1, 1, 2, 4, 5, 1]
