class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # Length check first
        if n1 + n2 != n3:
            return False
        
        # DP table where dp[i][j] = True if s1[0..i-1] and s2[0..j-1] can form s3[0..i+j-1]
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        
        # Fill dp
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        
        return dp[n1][n2]
sol = Solution()

print(sol.isInterleave("AAB", "AAC", "AAAABC"))  # True
print(sol.isInterleave("AB", "C", "ACB"))        # True
print(sol.isInterleave("YX", "X", "XXY"))        # False
print(sol.isInterleave("abc", "def", "adbcef"))  # True
print(sol.isInterleave("abc", "def", "abdecf"))  # True
