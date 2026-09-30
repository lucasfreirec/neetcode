class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_buy = prices[0]
        
        for i in range(1, len(prices)):
            best_buy = min(best_buy, prices[i-1])
            
            if prices[i] - best_buy > 0:
                profit = max(profit, prices[i] - best_buy)

        return profit #time: O(n), space: O(1)