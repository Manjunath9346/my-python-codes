class Solution:
    def findSum(self, s1, s2):
        # Reverse strings for easy addition from LSB
        i, j, carry, res = len(s1)-1, len(s2)-1, 0, []
        while i >= 0 or j >= 0 or carry:
            d1 = int(s1[i]) if i >= 0 else 0
            d2 = int(s2[j]) if j >= 0 else 0
            s = d1 + d2 + carry
            res.append(str(s % 10))
            carry = s // 10
            i, j = i-1, j-1
        return ''.join(reversed(res))
s = Solution()

print(s.findSum("25", "23"))     # "48"
print(s.findSum("2500", "23"))   # "2523"
print(s.findSum("2", "3"))       # "5"
print(s.findSum("99999", "1"))   # "100000"
