class Solution:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        if not digits or digits[0] == '0':
            return 0

        # dp[i] represents the number of ways to decode the substring of length i
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has 1 way to decode
        dp[1] = 1  # First character is already validated to be non-zero

        for i in range(2, n + 1):
            one_digit = int(digits[i - 1])
            two_digit = int(digits[i - 2:i])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

sol = Solution()
print(sol.countWays("123"))  # Output: 3
print(sol.countWays("90"))   # Output: 0
print(sol.countWays("05"))   # Output: 0
