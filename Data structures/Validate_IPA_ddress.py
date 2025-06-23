class Solution:
    def isValid(self, s):
        parts = s.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            if not 0 <= int(part) <= 255:
                return False
        return True
sol = Solution()

print(sol.isValid("222.111.111.111"))  # True
print(sol.isValid("5555..555"))        # False
print(sol.isValid("0.0.0.255"))        # True
print(sol.isValid("192.168.01.1"))     # False (leading 0 in "01")
print(sol.isValid("123.456.78.90"))    # False (456 > 255)
print(sol.isValid("172.16.254.1"))     # True
print(sol.isValid("172.16.254.01"))    # False (leading 0)
