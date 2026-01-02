class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        mid = (low + high) // 2
        while low <= high:
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                inner_low = 0
                inner_high = len(matrix[mid]) - 1
                inner_mid = (inner_low + inner_high) // 2
                while inner_low <= inner_high:
                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target < matrix[mid][inner_mid]:
                        inner_high = inner_mid - 1
                        inner_mid = (inner_low + inner_high) // 2
                    else:
                        inner_low = inner_mid + 1
                        inner_mid = (inner_low + inner_high) // 2
                return False
            elif target < matrix[mid][0]:
                high = mid - 1
                mid = (low + high) // 2
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                low = mid + 1
                mid = (low + high) // 2
        return False

# Runtime: Beats 100%
# Memory: Beats 93%

