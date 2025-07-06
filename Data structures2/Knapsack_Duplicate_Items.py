class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)
        dp = [0] * (capacity + 1)

        for c in range(capacity + 1):
            for i in range(n):
                if wt[i] <= c:
                    dp[c] = max(dp[c], dp[c - wt[i]] + val[i])
        
        return dp[capacity]
# Test case 1
val = [1, 1]
wt = [2, 1]
capacity = 3
print(Solution().knapSack(val, wt, capacity))  # Output: 3

# Test case 2
val = [6, 1, 7, 7]
wt = [1, 3, 4, 5]
capacity = 8
print(Solution().knapSack(val, wt, capacity))  # Output: 48

# Test case 3
val = [6, 8, 7, 100]
wt = [2, 3, 4, 5]
capacity = 1
print(Solution().knapSack(val, wt, capacity))  # Output: 0
