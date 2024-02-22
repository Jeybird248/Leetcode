class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n*n)]
        
        for i in range(n):
            self.parent[i] = 0
            self.parent[(n-1)*n + i] = 0
        
        for i in range(n):
            self.parent[i*n] = 0
            self.parent[(n-1) + i*n] = 0

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
            
        else:
            return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parent[py] = px
        
        return px == py

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        ans = 0
        n = len(grid) + 1
        dsu = DSU(n)
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == "/":
                    ans += dsu.union(i*n + j + 1, (i+1)*n + j)
                
                elif x == "\\":
                    ans += dsu.union(i*n + j, (i+1)*n + j + 1)
        
        return ans + 1