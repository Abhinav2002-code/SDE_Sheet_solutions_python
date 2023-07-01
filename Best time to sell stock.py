class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        min = sys.maxsize
        maxPro = 0
        for i in range(n):
            if(prices[i] < min):
                min = prices[i]
            if ((prices[i] - min) > maxPro):
                maxPro = prices[i] -min
        return maxPro
