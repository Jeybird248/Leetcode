class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Directions for all 8 possible neighbors (including diagonals)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        rows, cols = len(board), len(board[0])
        
        # Step 1: Update board in-place with future state indicators:
        # -1: was alive, now dead
        # 2: was dead, now alive
        
        for i in range(rows):
            for j in range(cols):
                live_neighbors = 0
                
                # Count live neighbors
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < rows and 0 <= nj < cols and abs(board[ni][nj]) == 1:
                        live_neighbors += 1
                
                # Apply Game of Life rules
                if board[i][j] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # Alive to dead
                else:  # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 2  # Dead to alive
        
        # Step 2: Finalize board state (replace -1 with 0, and 2 with 1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0  # Now dead
                elif board[i][j] == 2:
                    board[i][j] = 1  # Now alive
