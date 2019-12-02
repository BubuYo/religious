class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top, left = 0, 0
        button, right = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        direction = 0
        while left <= right and top <= button:
            if direction % 4 == 0:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            if direction % 4 == 1:
                for i in range(top, button + 1):
                    result.append(matrix[i][right])
                right -= 1
            if direction % 4 == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[button][i])
                button -= 1
            if direction % 4 == 3:
                for i in range(button, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

            direction += 1
        return result
