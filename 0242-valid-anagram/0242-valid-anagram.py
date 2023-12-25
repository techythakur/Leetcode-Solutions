from collections import *
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        for i,j in count_t.items():
            if j!=count_s[i]:
                return False
        return True