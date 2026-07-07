class Solution:
    def searchMatrix(self, matrix, target):
        j, i = len(matrix[0]) - 1, 0
        while j >= 0 and i < len(matrix):
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False