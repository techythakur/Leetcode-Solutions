class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=-1
                    col[j]=-1
                    
        for i in range(m):
            if row[i]==-1:
                matrix[i]=[0]*n
        
        for i in range(n):
            if col[i]==-1:
                for j in range(m):
                    matrix[j][i]=0
        return matrix
        