class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0) ]
        def bfs(x, y):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                grid[y][x] = "-1"
                for d in directions:
                    if 0 <= x + d[0] < len(grid[0]) and 0 <= y + d[1] < len(grid) and grid[y + d[1]][x + d[0]] == "1":
                        bfs(x + d[0], y + d[1])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(j, i)
                    count += 1
        
        return count