class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[]
        for i in range(len(s)):
            res+= [[s[i],indices[i]]]
        res.sort(key= lambda x: x[1])
        result=""
        for i in range(len(s)):
            result+=res[i][0]
        return result