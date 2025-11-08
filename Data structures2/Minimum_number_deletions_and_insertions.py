class Solution:
	def minOperations(self, s1, s2):
		n, m = len(s1), len(s2)
		
		# Find LCS (Longest Common Subsequence)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if s1[i - 1] == s2[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
					_
		lcs = dp[n][m]
		
		# Minimum operations = deletions + insertions
		return (n - lcs) + (m - lcs)
sol = Solution()

print(sol.minOperations("heap", "pea"))            #  Output: 3
print(sol.minOperations("geeksforgeeks", "geeks")) #  Output: 8
print(sol.minOperations("abcd", "anc"))            #  Output: 3
print(sol.minOperations("a", "a"))                 #  Output: 0
print(sol.minOperations("abc", "def"))             #  Output: 6
