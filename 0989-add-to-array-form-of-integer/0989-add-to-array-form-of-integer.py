class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number=""
        for i in num:
            number+=str(i)
        result=int(number)+k
        res=[]
        for i in str(result):
            res.append(int(i))
        return res