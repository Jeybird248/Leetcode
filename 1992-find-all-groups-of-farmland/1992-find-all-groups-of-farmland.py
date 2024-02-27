from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def explore(x, y):
            x_end, y_end = x, y

            # Explore right
            while y_end + 1 < n and land[x][y_end + 1] == 1:
                y_end += 1

            # Explore down
            while x_end + 1 < m and land[x_end + 1][y] == 1:
                x_end += 1

            # Mark the explored farmland as 0
            for i in range(x, x_end + 1):
                for j in range(y, y_end + 1):
                    land[i][j] = 0

            return [x, y, x_end, y_end]

        m, n = len(land), len(land[0])
        result = []

        for x in range(m):
            for y in range(n):
                if land[x][y] == 1:
                    result.append(explore(x, y))

        return result
