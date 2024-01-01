class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i=0
        j=0
        maxm=0
        lst=[]
        while(i<len(s)):
            charI=s[i]
            while(charI in lst):
                lst.pop(lst.index(s[j]))
                j+=1
            lst.append(charI)
            maxm=max(maxm,i-j+1)
            i+=1
        return maxm