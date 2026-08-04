class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        result = []
        direction = RIGHT

        while len(result) != (m * n):
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    result.append(matrix[i][j])
                    j += 1
                direction = DOWN
                i += 1
                j -= 1
                RIGHT_WALL -= 1

            elif direction == DOWN:
                while i < DOWN_WALL:
                    result.append(matrix[i][j])
                    i += 1
                direction = LEFT
                i -= 1
                j -= 1
                DOWN_WALL -= 1

            elif direction == LEFT:
                while j > LEFT_WALL:
                    result.append(matrix[i][j])
                    j -= 1
                direction = UP
                i -= 1
                j += 1
                LEFT_WALL += 1

            elif direction == UP:
                while i > UP_WALL:
                    result.append(matrix[i][j])
                    i -= 1
                direction = RIGHT
                i += 1
                j += 1
                UP_WALL += 1

        return result


sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix))

