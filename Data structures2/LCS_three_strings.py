class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        # Initialize 3D DP array
        dp = [[[0]*(n3+1) for _ in range(n2+1)] for __ in range(n1+1)]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                for k in range(1, n3+1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
        
        return dp[n1][n2][n3]
sol = Solution()

# Test 1
print(sol.lcsOf3("geeks", "geeksfor", "geeksforgeeks"))  
# Output: 5

# Test 2
print(sol.lcsOf3("abcd1e2", "bc12ea", "bd1ea"))  
# Output: 3

# Test 3
print(sol.lcsOf3("abc", "abc", "abc"))  
# Output: 3

# Test 4
print(sol.lcsOf3("abc", "def", "ghi"))  
# Output: 0
