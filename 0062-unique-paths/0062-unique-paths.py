class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(n):
            grid[0][i] = 1
        for i in range(m):
            grid[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                grid[j][i] = grid[j - 1][i] + grid[j][i - 1]
        return grid[m - 1][n - 1]