class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        
        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i-1])
            
            if prices[i] - min_buy > 0:
                profit = max(profit, prices[i] - min_buy)

        return profit