class Solution:
    def findNth(self, n):
        result = 0
        place = 1
        while n > 0:
            result += (n % 9) * place
            n //= 9
            place *= 10
        return result
obj = Solution()

print(obj.findNth(8))   # ➤ 8
print(obj.findNth(9))   # ➤ 10
print(obj.findNth(10))  # ➤ 11
print(obj.findNth(20))  # ➤ 22
print(obj.findNth(100)) # ➤ 123
