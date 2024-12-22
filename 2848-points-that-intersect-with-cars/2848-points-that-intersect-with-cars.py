class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()
        for i in nums:
            res |= set(range(i[0],i[1]+1))
        return len(res)