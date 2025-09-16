class Solution:
    def evaluatePostfix(self, arr):
        stack = []
        
        for token in arr:
            if token.lstrip('-').isdigit():  # operand
                stack.append(int(token))
            else:  # operator
                b, a = stack.pop(), stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # floor division (handles negatives correctly)
                    stack.append(a // b)
                elif token == '^':
                    stack.append(a ** b)
        
        return stack[-1]
s = Solution()

print(s.evaluatePostfix(["2", "3", "1", "*", "+", "9", "-"]))  
# -4

print(s.evaluatePostfix(["2", "3", "^", "1", "+"]))  
# 9

print(s.evaluatePostfix(["-8", "3", "/"]))  
# -3   (correct floor division)
