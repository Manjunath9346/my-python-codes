class Solution:
    def maxLen(ob, s):
        stack = [-1]  # Initialize stack with base for valid substring
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)  # reset base index

        return max_len
s = "(()("
print(Solution().maxLen(s))  # Output: 2
s = "()(())("
print(Solution().maxLen(s))  # Output: 6
s = "(()())"
print(Solution().maxLen(s))  # Output: 6
