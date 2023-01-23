class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={}
        check=defaultdict(int)
        for i in trust:
            d[i[0]]=i[1] 
            check[i[1]]+=1  
    
        for i in range(1,n+1):
            if d.get(i) is None and check[i]==n-1:
                return i

        return -1