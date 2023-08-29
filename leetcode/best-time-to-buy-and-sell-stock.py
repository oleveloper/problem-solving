# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprofit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[r] > prices[l]:
                maxprofit = max(maxprofit, profit)
            else:
                l = r
            r += 1
        
        return maxprofit
