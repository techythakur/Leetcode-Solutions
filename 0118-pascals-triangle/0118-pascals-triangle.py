class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op=[[1]]
        for i in range(numRows-1):
            temp=[0]+op[-1]+[0]
            row=[]
            for j in range(len(op[-1])+1):
                row.append(temp[j]+temp[j+1])
            op.append(row)
        return op