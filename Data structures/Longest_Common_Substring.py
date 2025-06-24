# User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        n = len(s1)
        m = len(s2)
        
        # Create a 2D array to store lengths of longest common suffixes
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        result = 0

        # Build the dp array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        return result
sol = Solution()

print(sol.longestCommonSubstr("ABCDGH", "ACDGHR"))  # Output: 4 ("CDGH")
print(sol.longestCommonSubstr("abc", "acb"))        # Output: 1 ("a", "b", or "c")
print(sol.longestCommonSubstr("YZ", "yz"))          # Output: 0 (case-sensitive)
print(sol.longestCommonSubstr("abcde", "cdefg"))    # Output: 3 ("cde")
