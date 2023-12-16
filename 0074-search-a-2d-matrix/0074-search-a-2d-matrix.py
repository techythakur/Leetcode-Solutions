class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][-1] and target in matrix[i]:
                return True
        return False