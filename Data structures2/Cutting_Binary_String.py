class Solution:
    def cuts(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # no cuts for empty prefix

        def is_power_of_5(bin_str):
            if bin_str[0] == '0':
                return False
            num = int(bin_str, 2)
            while num > 1:
                if num % 5 != 0:
                    return False
                num //= 5
            return True

        for i in range(1, n + 1):
            for j in range(i):
                if is_power_of_5(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1
sol = Solution()

print(sol.cuts("101101101"))   # Output: 3 → "101" (5), "101" (5), "101" (5)
print(sol.cuts("1111101"))     # Output: 1 → "1111101" = 125
print(sol.cuts("00000"))       # Output: -1 → No valid power of 5
print(sol.cuts("101"))         # Output: 1 → "101" = 5
print(sol.cuts("1101"))        # Output: -1 → No valid cuts
