from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        
        # Loop through the price array
        for i in range(1, n):
            # If today's price is higher than yesterday's, we gain profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
sol = Solution()

# Test Case 1
print(sol.maximumProfit([100, 180, 260, 310, 40, 535, 695]))
# Output: 865

# Test Case 2
print(sol.maximumProfit([4, 2, 2, 2, 4]))
# Output: 2

# Test Case 3 (No profit)
print(sol.maximumProfit([5, 4, 3, 2, 1]))
# Output: 0

# Test Case 4 (All increasing)
print(sol.maximumProfit([1, 2, 3, 4, 5]))
# Output: 4
