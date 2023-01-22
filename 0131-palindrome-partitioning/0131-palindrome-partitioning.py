class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        
        def helper(path,ind):
            if ind==len(s):
                res.append(path[::])
                return
            
            for i in range(ind,len(s)):
                if isPal(s,ind,i):
                    path.append(s[ind:i+1])
                    helper(path,i+1)
                    path.pop()
        def isPal(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        helper([],0)
        return res