class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n_row, n_col, self.res, seen = len(mat), len(mat[0]), float('inf'), {}
        
        def flip(row,col):
            for x, y in ((row,col),(row-1,col),(row+1,col),(row,col-1),(row,col+1)):
                if 0<=x<=n_row-1 and 0<=y<=n_col-1: mat[x][y] ^= 1

        def dfs(steps,path):
            
            # if the the flipped cells (regardless of order) is seen or steps greater than any known solution, prune
            if tuple(sorted(path)) in seen or steps>=self.res:
                return
            else:
                # mark this sequence as seen so no repetition in other branches
                seen[tuple(sorted(path))]=True
            
            # if all digits are 0's
            if all(all(not cell for cell in row) for row in mat):
                if self.res > steps:
                    self.res = steps
                return
                
            for i in range(n_row):
                for j in range(n_col):
                    # if the cell has not been flipped before
                    if (i,j) not in path:
                        # print(path)
                        # flip
                        flip(i,j)
                        dfs(steps+1,path+[(i,j)])
                        # reverse the operation for use in other branches
                        flip(i,j)

        dfs(0,[])
        return self.res if self.res!=float(inf) else -1	