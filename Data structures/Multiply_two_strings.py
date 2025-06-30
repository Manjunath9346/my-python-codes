class Solution:
    def multiplyStrings(self, s1, s2):
        # Handle signs
        negative = False
        if s1[0] == '-' and s2[0] != '-':
            negative = True
            s1 = s1[1:]
        elif s1[0] != '-' and s2[0] == '-':
            negative = True
            s2 = s2[1:]
        elif s1[0] == '-' and s2[0] == '-':
            s1 = s1[1:]
            s2 = s2[1:]

        # Remove leading zeros
        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'

        # Early return if one of them is 0
        if s1 == '0' or s2 == '0':
            return "0"

        n, m = len(s1), len(s2)
        res = [0] * (n + m)

        # Reverse both numbers for easier index handling
        s1 = s1[::-1]
        s2 = s2[::-1]

        # Multiply digit by digit
        for i in range(n):
            for j in range(m):
                res[i + j] += (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Remove leading zeros from result
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # Convert to string
        result_str = ''.join(map(str, res[::-1]))

        # Add negative sign if needed
        return '-' + result_str if negative else result_str
print(Solution().multiplyStrings("0033", "2"))     # Output: "66"
print(Solution().multiplyStrings("11", "23"))      # Output: "253"
print(Solution().multiplyStrings("123", "0"))      # Output: "0"
print(Solution().multiplyStrings("-12", "10"))     # Output: "-120"
print(Solution().multiplyStrings("-12", "-10"))    # Output: "120"
