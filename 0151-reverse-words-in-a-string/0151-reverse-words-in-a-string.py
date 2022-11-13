class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split()
        res=temp[::-1]
        return " ".join(res)