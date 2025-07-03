class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1

        char_map = {}
        left = 0
        max_len = -1

        for right in range(n):
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            if len(char_map) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
sol = Solution()

print(sol.longestKSubstr("aabacbebebe", 3))  # Output: 7
print(sol.longestKSubstr("aaaa", 2))         # Output: -1
print(sol.longestKSubstr("aabaaab", 2))      # Output: 7
print(sol.longestKSubstr("abcabcabc", 3))    # Output: 9
print(sol.longestKSubstr("abc", 4))          # Output: -1
