class Solution:
    def binstr(self, n):
        result = []
        for i in range(2 ** n):
            # format i as binary with n bits, padding with zeros
            result.append(format(i, '0{}b'.format(n)))
        return result
s = Solution()
print(s.binstr(2))  
# ['00', '01', '10', '11']

print(s.binstr(3))  
# ['000', '001', '010', '011', '100', '101', '110', '111']
