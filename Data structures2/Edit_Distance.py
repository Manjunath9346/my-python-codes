class Solution:
    def editDistance(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  # Need j insertions
                elif j == 0:
                    dp[i][j] = i  # Need i deletions
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1],    # Insert
                        dp[i-1][j],    # Delete
                        dp[i-1][j-1]   # Replace
                    )
        return dp[m][n]
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ("geek", "gesek", 1),
        ("gfg", "gfg", 0),
        ("abcd", "bcfe", 3),
        ("intention", "execution", 5)  # extra test case
    ]
    
    for s1, s2, expected in test_cases:
        result = obj.editDistance(s1, s2)
        print(f"s1='{s1}', s2='{s2}' | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
