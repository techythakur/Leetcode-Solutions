class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in nums:
            if j > nums[i]:
                i+=1
                nums[i]=j
        return i+1
        '''nums[:] = sorted(set(nums))
        return len(nums)'''