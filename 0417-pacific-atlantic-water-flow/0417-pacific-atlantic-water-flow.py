from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Grids to track reachability to Pacific and Atlantic
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        # Directions for moving: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, reachable):
            # mark current cell as reachable
            reachable[r][c] = True

            # explore the neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check if new position is within bounds and hasn't been visited,
                # and if the height at (nr, nc) is >= height at (r, c)
                if (0 <= nr < m and 0 <= nc < n and 
                    not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # Run DFS from the Pacific border (top and left edges)
        for r in range(m):
            dfs(r, 0, pacific_reachable)  # Left edge (Pacific)
            dfs(r, n-1, atlantic_reachable)  # Right edge (Atlantic)

        for c in range(n):
            dfs(0, c, pacific_reachable)  # Top edge (Pacific)
            dfs(m-1, c, atlantic_reachable)  # Bottom edge (Atlantic)

        # Collect cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result
