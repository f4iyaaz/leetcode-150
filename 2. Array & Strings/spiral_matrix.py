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

        while result != (m * n):
            pass

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix))

