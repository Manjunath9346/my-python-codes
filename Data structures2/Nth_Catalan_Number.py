class Solution:
    def findCatalan(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.findCatalan(3))  # Expected 5
    print(sol.findCatalan(4))  # Expected 14
    print(sol.findCatalan(1))  # Expected 1
