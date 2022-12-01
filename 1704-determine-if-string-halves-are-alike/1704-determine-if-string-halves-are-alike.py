class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[:n//2]
        b=s[n//2:]
        vowels="aeiouAEIOU"
        ca=0
        cb=0
        i=0
        while i<n//2:
            if a[i] in vowels:
                ca+=1
            if b[i] in vowels:
                cb+=1
            i+=1
        
        return ca==cb
            