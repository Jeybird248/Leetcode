class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    counter += 1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        timer = 0
        while q and counter:
            temp = []
            while q:
                pair = q.pop(0)
                for d in directions:
                    if 0 <= pair[0] + d[0] < len(grid) and 0 <= pair[1] + d[1] < len(grid[0]) and grid[pair[0] + d[0]][pair[1] + d[1]] == 1:
                        temp.append((pair[0] + d[0], pair[1] + d[1]))
                        grid[pair[0]+ d[0]][pair[1]+ d[1]] = 2
                        counter -= 1
            q = temp
            if temp:
                timer += 1
        return timer if counter == 0 else -1