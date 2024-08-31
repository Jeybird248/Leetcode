class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        fresh = 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            time += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # Check if the neighboring cell is within bounds and is a fresh orange.
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot the fresh orange
                        fresh -= 1  # Decrease the count of fresh oranges
                        q.append((nx, ny))

                if fresh == 0:
                    return time
    
        # If we exit the loop and there are still fresh oranges left, return -1.
        return -1