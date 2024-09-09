class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]) - 1, 0
        while 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
            if matrix[y][x] == target:
                return True
            if  matrix[y][x] > target:
                x -= 1
            else:
                y += 1
        return False