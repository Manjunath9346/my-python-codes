class Solution:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Add an element to the top of Stack
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    # Returns top element of Stack
    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    # Finds minimum element of Stack
    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
s = Solution()
queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
results = []

for query in queries:
    if query[0] == 1:
        s.push(query[1])
    elif query[0] == 2:
        s.pop()
    elif query[0] == 3:
        results.append(s.peek())
    elif query[0] == 4:
        results.append(s.getMin())

print(results)  # Output: [3, 2, 1]
