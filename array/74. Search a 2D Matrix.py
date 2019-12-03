class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_index = -1
        for j in range(len(matrix)):
            if matrix[j][0] == target:
                return True
            if matrix[j][0] > target:
                row_index = j - 1
                break
        for i in range(len(matrix[row_index])):
            if matrix[row_index][i] == target:
                return True
        return False
