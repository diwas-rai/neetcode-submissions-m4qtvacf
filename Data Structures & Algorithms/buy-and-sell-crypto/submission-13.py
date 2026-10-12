class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0

        max_profit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            if prices[r] < prices[l]:
                l = r
        
        return max_profit