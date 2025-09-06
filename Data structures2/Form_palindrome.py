class Solution:
    def countMin(self, s):
        n = len(s)
        # dp[i][j] = length of longest palindromic subsequence in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # fill dp for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        lps = dp[0][n - 1]  # length of longest palindromic subsequence
        return n - lps      # min insertions = total length - lps

# Test Cases
sol = Solution()
print(sol.countMin("abcd"))    # Output: 3
print(sol.countMin("aa"))      # Output: 0
print(sol.countMin("abcda"))   # Output: 2
print(sol.countMin("race"))    # Output: 3
print(sol.countMin("a"))       # Output: 0
