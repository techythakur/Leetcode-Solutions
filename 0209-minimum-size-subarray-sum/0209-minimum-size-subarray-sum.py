class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = float('inf')
        curr = 0
        left = 0
        for right in range(len(nums)):
            curr += nums[right]
            
            while curr>=target:
                if right-left+1<minm:
                    minm = right-left+1
                
                curr-=nums[left]
                left+=1
        return minm if minm!=float('inf') else 0
        
        
        
        
        # if sum(nums)<target:
        #     return 0
        # minm = len(nums)
        # l,r=0,0
        # summ = 0
        # while r<len(nums):
        #     if nums[l]>=target or nums[r]>=target:
        #         return 1
        #     summ += nums[r]
        #     r+=1
        #     if summ>=target:
        #         while l<=r and summ>=target:
        #             summ-=nums[l]
        #             l+=1
        #         minm = min(r-l+1,minm)            
        # return minm
                
            