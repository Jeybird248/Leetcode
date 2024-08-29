class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # start on first row 
        # iterate through columns until free spot (use helper functiont o check validity)
        def is_valid(board, row, col):
            # Check this column on upper rows
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check upper left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check upper right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        # check next row for next queen
        # move to next row and keep searching
        # if can't find any seats in current row, remove last added queen
        # keep going until all queens are placed, then add current board to output array 
        def solve(row):
            if row == n:  # All queens are placed
                solutions.append(["".join(r) for r in board])
                return

            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'  # Place queen
                    solve(row + 1)         # Recurse to place next queen
                    board[row][col] = '.'  # Backtrack, remove the queen
                    
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        solve(0)
        return solutions
        