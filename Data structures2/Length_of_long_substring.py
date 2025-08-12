class Solution:
    def longestUniqueSubstring(self, s):
        last_index = {}
        left = 0
        max_len = 0
        
        for right, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1
            last_index[ch] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
sol = Solution()
print(sol.longestUniqueSubstring("geeksforgeeks"))  # Output: 7
print(sol.longestUniqueSubstring("abdefgabef"))     # Output: 6
print(sol.longestUniqueSubstring("aaaaa"))          # Output: 1
print(sol.longestUniqueSubstring("abcabcbb"))       # Output: 3
print(sol.longestUniqueSubstring("pwwkew"))         # Output: 3
