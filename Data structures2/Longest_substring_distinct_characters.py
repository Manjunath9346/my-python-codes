class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        last_seen = {}
        max_len = 0
        start = 0

        for end in range(n):
            if s[end] in last_seen and last_seen[s[end]] >= start:
                start = last_seen[s[end]] + 1
            last_seen[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
sol = Solution()

# Test Case 1
print(sol.longestUniqueSubstr("geeksforgeeks"))  # Output: 7 ("eksforg")

# Test Case 2
print(sol.longestUniqueSubstr("aaa"))            # Output: 1 ("a")

# Test Case 3
print(sol.longestUniqueSubstr("abcdefabcbb"))    # Output: 6 ("abcdef")

# Test Case 4
print(sol.longestUniqueSubstr("abcabcbb"))       # Output: 3 ("abc")

# Test Case 5
print(sol.longestUniqueSubstr("abccdefgh"))      # Output: 7 ("cdefgh")
