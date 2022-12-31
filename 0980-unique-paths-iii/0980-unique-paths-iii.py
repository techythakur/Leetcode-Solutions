class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        count=0
        
        a=0
        b=0
                
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==-1):
                    count+=1
                    
                if(grid[i][j]==1):
                    a=i
                    b=j
        
        def rec(i,j,visited):
            nonlocal count
            
            if(i<0 or j<0 or i==m or j==n):
                return 0
            
            if(grid[i][j]==2):
                #print(visited,m*n-count)
                
                if(visited==m*n-count):
                    #print('hi')
                    return 1
                
                else:
                    return 0
            
            if(grid[i][j]!=-1):
                grid[i][j]=-1
                
                a=rec(i+1,j,visited+1)
                b=rec(i-1,j,visited+1)
                c=rec(i,j+1,visited+1)
                d=rec(i,j-1,visited+1)
                
                grid[i][j]=0
                
                return a+b+c+d
            
            return 0
                    
        return rec(a,b,1)