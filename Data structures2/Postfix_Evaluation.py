class Solution:
    def evaluate(self, arr):
        stack = []
        for token in arr:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Python division rounding toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

# Test Cases
sol = Solution()
print(sol.evaluate(["2", "3", "1", "*", "+", "9", "-"]))  # Output: -4
print(sol.evaluate(["100", "200", "+", "2", "/", "5", "*", "7", "+"]))  # Output: 757
print(sol.evaluate(["4", "13", "5", "/", "+"]))  # Output: 6, because 13/5 = 2
print(sol.evaluate(["10", "6", "9", "3", "/", "-", "*"]))  # Output: 30
