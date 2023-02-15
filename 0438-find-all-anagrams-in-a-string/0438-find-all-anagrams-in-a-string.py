class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0 or len(p)==0:
            return []
        counter_p= Counter(p)
        res=[]
        for i in range(0,len(s)-len(p)+1):
            anagram=s[i:i+len(p)]
            counter_s = Counter(anagram)
            if counter_s==counter_p:
                res.append(i)
                i+=len(p)
        return res