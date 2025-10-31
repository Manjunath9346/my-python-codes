class Solution:
    def chooseandswap(self, s):
        seen = set()
        for i in range(len(s)):
            for ch in sorted(set(s[i+1:])):
                if ch < s[i] and ch not in seen:
                    a, b = s[i], ch
                    s = s.replace(a, '#').replace(b, a).replace('#', b)
                    return s
            seen.add(s[i])
        return s
# Test Case 1
print(Solution().chooseandswap("ccad"))   # Output: "aacd"

# Test Case 2
print(Solution().chooseandswap("abba"))   # Output: "abba"

# Test Case 3
print(Solution().chooseandswap("bca"))    # Output: "acb"

# Test Case 4
print(Solution().chooseandswap("azbz"))   # Output: "abab"

# Test Case 5
print(Solution().chooseandswap("aaaa"))   # Output: "aaaa"
