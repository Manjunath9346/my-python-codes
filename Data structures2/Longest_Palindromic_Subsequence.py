class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        rev = s[::-1]

        # Only keep two rows at a time
        prev = [0] * (n+1)
        curr = [0] * (n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rev[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, [0] * (n+1)

        return prev[n]
sol = Solution()
print(sol.longestPalinSubseq("bbabcbcab"))  # 7
print(sol.longestPalinSubseq("abcd"))       # 1
print(sol.longestPalinSubseq("agbdba"))     # 5
print(sol.longestPalinSubseq("a"*1000))     # 1000 (worst case, still fast)
