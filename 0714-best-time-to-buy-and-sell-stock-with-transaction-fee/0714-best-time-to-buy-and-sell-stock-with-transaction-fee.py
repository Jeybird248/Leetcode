class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        profit = 0
        bought = prices[0] + fee  # Initialize bought with the first price plus fee
        
        for price in prices[1:]:  # Start iterating from the second price
            if price + fee < bought:  # If the current price is lower than the cost of buying
                bought = price + fee  # Update the bought price
            elif price > bought:  # If the current price is higher than the bought price
                profit += price - bought  # Add the profit to the total profit
                bought = price  # Update the bought price
        
        return profit