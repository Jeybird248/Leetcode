class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]) - 1, 0
        while 0 <= x and y < len(matrix):
            print(matrix[y][x])
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            else:
                x -= 1
                
        return False