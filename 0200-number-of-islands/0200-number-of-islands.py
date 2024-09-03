class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def bfs(x, y, grid):
            if 0 > x or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == "0":
                return
            
            grid[y][x] = "0"
            
            bfs(x - 1, y, grid)
            bfs(x + 1, y, grid)
            bfs(x, y + 1, grid)
            bfs(x, y - 1, grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(j, i, grid)
                    count += 1
                    
        return count