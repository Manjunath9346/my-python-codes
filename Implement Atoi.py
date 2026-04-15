class Solution:
    def myAtoi(self, s):
        # code here
        l = len(s)
        num = 0
        sign = 1
        i = 0
        digi = 0
        while i < l and s[i].isspace():
            i += 1
        
        if i < l and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
        
        while i < l and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num = num * sign
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        return num
