class Solution:
    def maxProfit(self, prices) -> int:
        # code here
        pro = 0
        l = len(arr)-1
        for i in range(l):
            if prices[i] < prices[i+1]:
                pro += prices[i+1] - prices[i]
        return pro
