from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Create a DP table with the same dimensions as the grid
        dp = [[0] * cols for _ in range(rows)]
        
        # Initialize the starting point
        dp[0][0] = grid[0][0]
        
        # Fill in the first row (can only come from the left)
        for x in range(1, cols):
            dp[0][x] = dp[0][x - 1] + grid[0][x]
        
        # Fill in the first column (can only come from above)
        for y in range(1, rows):
            dp[y][0] = dp[y - 1][0] + grid[y][0]
        
        # Fill in the rest of the DP table
        for y in range(1, rows):
            for x in range(1, cols):
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + grid[y][x]
        
        # The bottom-right corner contains the minimum path sum
        return dp[rows - 1][cols - 1]
