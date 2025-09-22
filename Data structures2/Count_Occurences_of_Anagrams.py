from collections import Counter

class Solution:
    def search(self, pat, txt):
        k = len(pat)
        pat_count = Counter(pat)
        window_count = Counter(txt[:k])
        res = 0

        if pat_count == window_count:
            res += 1

        for i in range(k, len(txt)):
            window_count[txt[i]] += 1
            window_count[txt[i-k]] -= 1
            if window_count[txt[i-k]] == 0:
                del window_count[txt[i-k]]

            if window_count == pat_count:
                res += 1

        return res


# ---------- Test Cases ----------
sol = Solution()

print(sol.search("for", "forxxorfxdofr"))  # Output: 3
print(sol.search("aaba", "aabaabaa"))      # Output: 4
print(sol.search("abc", "cbaebabacd"))     # Output: 2
print(sol.search("aa", "aaaaa"))           # Output: 4
