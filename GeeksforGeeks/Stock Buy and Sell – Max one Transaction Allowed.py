class Solution:
    def maxProfit(self, prices):
        # code here
        mini = float('inf')
        maxi = float('-inf')
        k = 0
        l = len(prices)
        for i in range(l):
            if prices[i] < mini:
                mini = prices[i]    
            k = prices[i] - mini
            if k > maxi:
                maxi = k
        return maxi
