class Solution:
    def maxProfit(self, prices):
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for p in prices:
            buy1 = min(buy1, p)        # lowest price for 1st buy
            sell1 = max(sell1, p - buy1)  # best profit from 1st sell
            
            buy2 = min(buy2, p - sell1)   # effective price for 2nd buy
            sell2 = max(sell2, p - buy2)  # best profit from 2nd sell
        
        return sell2
Input:
prices = [10, 22, 5, 75, 65, 80]
Output:
87
Input:
prices = [2, 30, 15, 10, 8, 25, 80]
Output:
100
