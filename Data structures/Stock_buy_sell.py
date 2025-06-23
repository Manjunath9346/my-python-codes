class Solution:
    # Function to find the maximum profit by buying and selling stocks multiple times.
    def stockBuySell(self, arr):
        n = len(arr)
        profit = 0
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                profit += arr[i] - arr[i - 1]
        return profit
sol = Solution()

print(sol.stockBuySell([100, 180, 260, 310, 40, 535, 695]))  # Output: 865
print(sol.stockBuySell([4, 2, 2, 2, 4]))                     # Output: 2
print(sol.stockBuySell([4, 2]))                              # Output: 0
print(sol.stockBuySell([1, 5, 3, 8, 12]))                    # Output: 13 (Buy at 1, sell at 5 = 4; Buy at 3, sell at 12 = 9)
