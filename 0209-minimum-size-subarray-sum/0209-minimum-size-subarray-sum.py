class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        minm = len(nums)
        l,r=0,0
        summ = 0
        while r<len(nums):
            if nums[l]>=target or nums[r]>=target:
                return 1
            summ += nums[r]
            r+=1
            if summ>=target:
                while l<=r and summ>=target:
                    summ-=nums[l]
                    l+=1
                minm = min(r-l+1,minm)            
        return minm
                
            