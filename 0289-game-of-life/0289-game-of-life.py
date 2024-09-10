class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1)]
        
        def is_valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                live_neighbors = 0
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if is_valid(new_row, new_col) and abs(board[new_row][new_col]) == 1:
                        live_neighbors += 1
                
                # If cell is dead and has exactly 3 live neighbors, it becomes alive.
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2  # Dead to alive transition
                
                # If cell is alive and does not have 2 or 3 live neighbors, it dies.
                if board[row][col] == 1 and not (2 <= live_neighbors <= 3):
                    board[row][col] = -1  # Alive to dead transition
        
        # Final pass to update the board.
        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 1  # Mark cells that became alive
                elif board[row][col] == -1:
                    board[row][col] = 0  # Mark cells that died
