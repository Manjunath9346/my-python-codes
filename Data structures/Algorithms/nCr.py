class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        MOD = 10**9 + 7
        dp = [[0 for _ in range(r+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(min(i, r)+1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        return dp[n][r]
sol = Solution()

# Test Case 1: Normal case
print("5C2 =", sol.nCr(5, 2))  # Expected Output: 10

# Test Case 2: r > n
print("2C4 =", sol.nCr(2, 4))  # Expected Output: 0

# Test Case 3: r = 0
print("5C0 =", sol.nCr(5, 0))  # Expected Output: 1

# Test Case 4: n = r
print("4C4 =", sol.nCr(4, 4))  # Expected Output: 1

# Test Case 5: Large n and small r
print("100C1 =", sol.nCr(100, 1))  # Expected Output: 100

# Test Case 6: Edge case
print("1C1 =", sol.nCr(1, 1))  # Expected Output: 1
