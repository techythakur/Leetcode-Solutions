class Solution:
    def numTilings(self, n: int) -> int:
        prev, curr, tri = 1, 1, 0                               
        for i in range(1,n):                                    
            prev, curr, tri = curr, prev+curr+2*tri, prev+tri   
        return curr%1000000007  