class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix))
        matrix[:] = [row[::-1] for row in matrix]
