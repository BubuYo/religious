class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_count = len(matrix)
        col_count = len(matrix[0])
        r, c = [], []
        for i in range(len(matrix)):
            for j in range(col_count):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        for i in r:
            matrix[i] = [0] * col_count
        for i in c:
            for j in range(row_count):
                matrix[j][i] = 0
