class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Count the occurrences of each row
        row_count = Counter(tuple(row) for row in grid)
        # Count the occurrences of each column
        col_count = Counter(tuple(col) for col in zip(*grid))
        
        # Calculate the total number of equal pairs
        count = 0
        for row in row_count:
            if row in col_count:
                count += row_count[row] * col_count[row]
        
        return count