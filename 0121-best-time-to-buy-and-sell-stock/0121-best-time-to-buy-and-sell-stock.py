class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = currP = 0
        left = right = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                currP = max(currP, prices[right] - prices[left])
                maxP = max(maxP, currP)
            else:
                currP = 0
                left = right
            right += 1
        return maxP