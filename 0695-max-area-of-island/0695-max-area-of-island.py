class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # Base cases:
            # If the cell is out of bounds or water (0) or already visited, return 0
            bounds = (r < 0 or r == rows or c < 0 or c == cols)
            if (bounds
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            # Mark the current cell as visited
            visit.add((r, c))
            # Explore adjacent cells in all four directions and count the area
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        # Initialize the maximum area of the island
        area = 0
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell represents land (1) and hasn't been visited yet
                if grid[r][c] == 1 and (r, c) not in visit:
                    # Calculate the area of the island starting from this cell
                    area = max(area, dfs(r, c))
        # Return the maximum area of the island
        return area