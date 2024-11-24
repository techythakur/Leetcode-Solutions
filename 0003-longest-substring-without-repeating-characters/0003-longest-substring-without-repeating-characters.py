class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = []
        maxm = 0
        for i in s:
            if i in curr:
                while curr and i in curr:
                    curr.pop(0)
            curr.append(i)
            maxm = max(len(curr), maxm)
        return maxm
                    