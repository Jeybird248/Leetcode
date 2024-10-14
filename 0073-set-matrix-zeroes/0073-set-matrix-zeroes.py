class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the matrix in-place to set entire rows and columns to zero where matrix[i][j] == 0.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero = col_zero = False

        # Step 1: Use the first row and first column as markers.
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0: row_zero = True
                    if j == 0: col_zero = True
                    matrix[i][0] = 0  # mark row
                    matrix[0][j] = 0  # mark column

        # Step 2: Use markers to set other elements to zero.
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row and first column separately.
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0
