class Solution:
    def spiralOrder(self, matrix):
        row_length = len(matrix[0])
        row = len(matrix)
        dummy_result = []

        # I think a while loop would be more suitable here instead of for loop
        for i in range(row_length):
            for num in matrix[i]:
                dummy_result.append(num)

        return dummy_result

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix))

