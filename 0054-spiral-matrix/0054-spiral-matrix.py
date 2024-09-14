from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        x = y = 0
        right = len(matrix[0]) - 1
        left = 0
        up = 0
        down = len(matrix) - 1
        
        direction = "right"
        output = []
        
        while len(output) < len(matrix) * len(matrix[0]):
            if direction == "right":
                while x <= right:
                    output.append(matrix[y][x])
                    x += 1
                x -= 1  # correct position after overshooting
                y += 1
                up += 1
                direction = "down"
            
            elif direction == "down":
                while y <= down:
                    output.append(matrix[y][x])
                    y += 1
                y -= 1  # correct position after overshooting
                x -= 1
                right -= 1
                direction = "left"
            
            elif direction == "left":
                while x >= left:
                    output.append(matrix[y][x])
                    x -= 1
                x += 1  # correct position after overshooting
                y -= 1
                down -= 1
                direction = "up"
            
            elif direction == "up":
                while y >= up:
                    output.append(matrix[y][x])
                    y -= 1
                y += 1  # correct position after overshooting
                x += 1
                left += 1
                direction = "right"
        
        return output
