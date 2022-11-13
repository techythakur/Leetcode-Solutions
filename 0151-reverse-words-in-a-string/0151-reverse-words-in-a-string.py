class Solution:
    def reverseWords(self, s: str) -> str:
        temp=list(map(str,s.split()))
        res=temp[::-1]
        return " ".join(res)