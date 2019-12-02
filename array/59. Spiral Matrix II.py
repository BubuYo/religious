class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        top, left = 0, 0
        button, right = n - 1, n - 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        direction = 0
        v = 0
        while left <= right and top <= button:
            if direction % 4 == 0:
                for i in range(left, right + 1):
                    v += 1
                    result[top][i] = v
                top += 1
            if direction % 4 == 1:
                for i in range(top, button + 1):
                    v += 1
                    result[i][right] = v
                right -= 1
            if direction % 4 == 2:
                for i in range(right, left - 1, -1):
                    v += 1
                    result[button][i] = v
                button -= 1
            if direction % 4 == 3:
                for i in range(button, top - 1, -1):
                    v += 1
                    result[i][left] = v
                left += 1

            direction += 1
        return result
