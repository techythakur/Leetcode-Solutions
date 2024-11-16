class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans=''
        for i in range(len(s)-1, -1, -1):
            if s[i] != '-':                
                if len(ans) % (k+1) == k:
                    ans += '-'
                ans += s[i].upper()         
        ans = ans [::-1]
        return ans