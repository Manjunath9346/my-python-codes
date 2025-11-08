class Solution:
    def removeKdig(self, s, k):
        stack = []

        for digit in s:
            # While the stack top is greater than the current digit, remove it
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k is still left, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert to string and remove leading zeros
        res = ''.join(stack).lstrip('0')
        return res if res else "0"
sol = Solution()

print(sol.removeKdig("4325043", 3))   #  Output: "2043"
print(sol.removeKdig("765028321", 5)) #  Output: "221"
print(sol.removeKdig("10", 1))        #  Output: "0"
print(sol.removeKdig("12345", 2))     #  Output: "123"
print(sol.removeKdig("100200", 1))    #  Output: "200"
