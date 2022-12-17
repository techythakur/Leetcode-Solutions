class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[1]*m
        col=[1]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
        
        for i in range(m):
            if row[i]==0:
                matrix[i]=[0]*n
        for i in range(n):
            if col[i]==0:
                for j in range(m):
                    matrix[j][i]=0
        return matrix