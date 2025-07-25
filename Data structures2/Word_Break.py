class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string is always valid

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
s = "ilikegfg"
dictionary = ["i", "like", "man", "india", "gfg"]
sol = Solution()
print(sol.wordBreak(s, dictionary))  # Output: True
