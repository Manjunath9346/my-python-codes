class Solution:
    def countFriendsPairings(self, n):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
        return dp[n]
sol = Solution()
print(sol.countFriendsPairings(3))  # Output: 4
print(sol.countFriendsPairings(2))  # Output: 2
print(sol.countFriendsPairings(1))  # Output: 1
print(sol.countFriendsPairings(4))  # Output: 10
