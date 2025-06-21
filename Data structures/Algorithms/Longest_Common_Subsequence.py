class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)
        
        # Initialize a 2D DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill the table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
sol = Solution()
print(sol.lcs("ABCDGH", "AEDFHR"))  # Output: 3
print(sol.lcs("ABC", "AC"))         # Output: 2
print(sol.lcs("XYZW", "XYWZ"))      # Output: 3
