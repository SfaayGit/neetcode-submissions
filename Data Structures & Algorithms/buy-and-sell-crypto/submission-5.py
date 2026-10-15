class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(len(prices)):
            while prices[right] < prices[left]:
                left+=1
            profit = max(profit, prices[right]-prices[left])
        return profit