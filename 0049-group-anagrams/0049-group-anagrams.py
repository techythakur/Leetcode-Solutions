class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        res = {}
        for i in strs:
            sorte = "".join(sorted(i))
            if sorte in res:
                res[sorte].append(i)
            else:
                res[sorte]=[i]
        
        return res.values()
            
            