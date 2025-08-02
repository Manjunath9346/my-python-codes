class Solution:
    def LongestRepeatingSubsequence(self, s):
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][n]
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ("axxzxy", 2),
        ("axxxy", 2),
        ("aab", 1),
        ("abc", 0)  # No repeating subsequence
    ]
    
    for s, expected in test_cases:
        result = obj.LongestRepeatingSubsequence(s)
        print(f"Input: '{s}' | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
