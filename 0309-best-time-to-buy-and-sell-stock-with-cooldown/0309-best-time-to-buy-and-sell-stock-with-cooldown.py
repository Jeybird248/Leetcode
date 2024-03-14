class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold_today = 0                # sold on current day
        bought = float('-inf')    # bought on current day 
        cooldown = 0                # cooldown on current day
        sold_yesterday = 0
        
        for price in prices:    
            sold_yesterday = sold_today
            
            sold_today = bought + price # bought previous day, sold now
            
            bought = max(bought, cooldown - price) # current money - price, buying
            
            cooldown = max(cooldown, sold_yesterday) # sold yesterday, updating
        return max(sold_today, cooldown)