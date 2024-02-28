from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid1), len(grid1[0])
        count = 0

        def traversal(x, y):
            # Base case: If coordinates are out of bounds or grid2 cell is already visited
            if not (0 <= x < row and 0 <= y < col) or grid2[x][y] == 0:
                return True
            
            # Mark the current cell as visited
            grid2[x][y] = 0
            
            # Explore neighboring cells
            check1 = traversal(x - 1, y)
            check2 = traversal(x + 1, y)
            check3 = traversal(x, y - 1)
            check4 = traversal(x, y + 1)
            
            # Check if the current cell is part of a valid sub-island
            return grid1[x][y] and check1 and check2 and check3 and check4

        # Iterate through each cell in grid2
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:  # If the cell is part of an unvisited island in grid2
                    if traversal(i, j):
                        count += 1  # Found a valid sub-island

        return count
