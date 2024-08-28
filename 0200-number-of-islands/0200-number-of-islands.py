class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(y, x, grid):
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == '0':
                return
        
            grid[y][x] = '0'
            bfs(y, x - 1, grid)
            bfs(y, x + 1, grid)
            bfs(y - 1, x, grid)
            bfs(y + 1, x, grid)
            
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j, grid)
                    count += 1
                    
        return count