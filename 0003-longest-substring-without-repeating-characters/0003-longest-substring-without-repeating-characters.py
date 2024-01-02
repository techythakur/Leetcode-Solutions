class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        lst = []
        i,j = 0,0
        maxm = 0
        while i<len(s):
            st = s[i]
            while st in lst:
                lst.pop(0)
                j+=1
            lst.append(st)
            maxm = max(maxm, i-j+1)
            i+=1
        return maxm
        