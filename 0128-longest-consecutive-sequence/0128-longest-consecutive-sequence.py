class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        nums.sort()
        res=set()
        maxm = 0
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1] or nums[i]==nums[i+1]:
                res.add(nums[i])
                res.add(nums[i+1])
                maxm = max(maxm, len(res))
            else:
                res=set()
        return maxm
            