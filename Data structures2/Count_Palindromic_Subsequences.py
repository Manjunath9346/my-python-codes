class Solution:
    def countPS(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Build the table
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
        
        return dp[0][n - 1]
sol = Solution()

print(sol.countPS("abcd"))  # Output: 4
print(sol.countPS("aab"))   # Output: 4
print(sol.countPS("b"))     # Output: 1
print(sol.countPS("aaa"))   # Output: 6 ('a','a','a','aa','aa','aaa')
print(sol.countPS("abcba")) # Output: 13
