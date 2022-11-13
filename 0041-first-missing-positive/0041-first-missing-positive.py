class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+2):
            if not i in nums:
                return i
        '''hashset=set(nums)
        for i in range(1,len(nums)+1):
            if i in hashset:
                continue
            else:
                return i
        return len(nums)+1'''