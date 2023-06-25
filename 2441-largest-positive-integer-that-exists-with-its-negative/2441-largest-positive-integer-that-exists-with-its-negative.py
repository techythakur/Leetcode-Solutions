class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums[::-1]:
            if -i in nums:
                return i
        return -1
        
        '''maxm=-1
        for i in range(len(nums)):
            if nums[i]<0 and nums[i]*-1 in nums:
                maxm=max(maxm,nums[i]*-1)
        return maxm'''