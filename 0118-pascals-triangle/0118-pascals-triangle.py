class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op=[[1]]
        for i in range(numRows-1):
            temp=[]
            res=[0]+op[-1]+[0]
            for i in range(1,len(res)):
                temp.append(res[i-1]+res[i])
            op.append(temp)
        return op
                