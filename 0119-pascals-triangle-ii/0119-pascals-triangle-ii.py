class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(rowIndex):
            if rowIndex == 0:
                return []
            if rowIndex == 1:
                return [[1]]

            prev_rows = pascal(rowIndex - 1)
            prev_row = prev_rows[-1]
            current_row = [1]

            for i in range(1, rowIndex - 1):
                current_row.append(prev_row[i - 1] + prev_row[i])

            current_row.append(1)
            prev_rows.append(current_row)

            return prev_rows
        
        return pascal(rowIndex + 1)[-1]