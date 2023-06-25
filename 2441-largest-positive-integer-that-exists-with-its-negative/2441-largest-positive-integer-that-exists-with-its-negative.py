class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxm=-1
        for i in range(len(nums)):
            if nums[i]<0 and nums[i]*-1 in nums:
                maxm=max(maxm,nums[i]*-1)
        return maxm