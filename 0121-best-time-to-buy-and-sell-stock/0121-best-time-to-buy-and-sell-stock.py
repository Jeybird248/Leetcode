class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        profit = 0

        for i in range(len(prices)):
            minValue = min(minValue, prices[i])
            profit = max(profit, prices[i]-minValue)
        
        return profit