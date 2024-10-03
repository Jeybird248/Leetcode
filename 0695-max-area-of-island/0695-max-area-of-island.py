class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.currCount = 0
        self.maxCount = 0
        directions = [(-1, 0),(1,0),(0,1),(0,-1)]
        
        def bfs(x, y):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == 1:
                grid[y][x] = -1
                self.currCount += 1 
                for d in directions:
                    bfs(x + d[0], y + d[1])
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.currCount = 0
                    bfs(j, i)
                    self.maxCount = max(self.maxCount, self.currCount)
        
        return self.maxCount

        