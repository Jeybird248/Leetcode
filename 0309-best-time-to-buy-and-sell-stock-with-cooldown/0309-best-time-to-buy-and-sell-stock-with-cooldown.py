class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0                # sold on current day
        hold = float('-inf')    # bought on current day 
        rest = 0                # cooldown on current day
        
        for price in prices:    
            prev_sold = sold
            
            sold = hold + price # bought previous day, sold now
            
            hold = max(hold, rest - price) # current money - price, buying
            
            rest = max(rest, prev_sold) # sold yesterday, updating
            # print(price, sold, hold, rest)
        return max(sold, rest)
    
    