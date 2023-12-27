class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortString(st):
            stl = [i for i in st]
            stl.sort()
            return "".join(stl)
        
        
        res = {}
        for i in strs:
            sorte = sortString(i)
            if sorte in res:
                res[sorte].append(i)
            else:
                res[sorte]=[i]
        
        return res.values()
            
            