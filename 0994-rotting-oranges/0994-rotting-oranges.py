from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh_count = 0
        # Initialize queue with all rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1
        
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # Possible 4 directions
        timer = 0
        
        while q and fresh_count > 0:
            new_rotten = []
            while q:  # Process the current rotten oranges
                point = q.pop(0)
                for direction in directions:
                    ni, nj = point[0] + direction[0], point[1] + direction[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  # Mark the orange as rotten
                        new_rotten.append((ni, nj))  # Add to new rotten list
                        fresh_count -= 1  # Decrease the fresh orange count
            
            q = new_rotten  # Move to the newly rotten oranges
            if new_rotten:
                timer += 1  # Increment the timer after processing one round
        
        return timer if fresh_count == 0 else -1  # Return -1 if there are fresh oranges left
