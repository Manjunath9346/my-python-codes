class Solution:
    def InfixtoPostfix(self, s):
        def precedence(op):
            if op == '^':
                return 3
            elif op in ('*', '/'):
                return 2
            elif op in ('+', '-'):
                return 1
            return 0

        output = []
        stack = []

        for ch in s:
            if ch.isalnum():  # Operand
                output.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('
            else:  # Operator
                while stack and precedence(stack[-1]) >= precedence(ch):
                    output.append(stack.pop())
                stack.append(ch)

        while stack:
            output.append(stack.pop())

        return ''.join(output)
if __name__ == "__main__":
    sol = Solution()
    print(sol.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i"))  # Expected abcd^e-fgh*+^*+i-
    print(sol.InfixtoPostfix("A*(B+C)/D"))  # Expected ABC+*D/
    print(sol.InfixtoPostfix("(a+b)*(c+d)"))  # Expected ab+cd+*
