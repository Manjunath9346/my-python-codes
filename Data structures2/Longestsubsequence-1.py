class Solution:
    def longestSubseq(self, arr):
        n = len(arr)
        dp = [1] * n  # dp[i] stores length of longest subsequence ending at i

        for i in range(1, n):
            for j in range(i):
                if abs(arr[i] - arr[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
arr = [10, 9, 4, 5, 4, 8, 6]
print(Solution().longestSubseq(arr))  # Output: 3

arr = [1, 2, 3, 4, 5]
print(Solution().longestSubseq(arr))  # Output: 5
