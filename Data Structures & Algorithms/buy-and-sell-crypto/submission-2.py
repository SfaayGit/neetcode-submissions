class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = prices[0]
        profit = 0
        for price in prices:
            if (price<currentMin):
                currentMin = price
            currProfit = price - currentMin
            if(currProfit > profit):
                profit = currProfit
        return profit