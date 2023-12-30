class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left,right=j+1, len(nums)-1
                while left<right:
                    if nums[i]+nums[j]+nums[right]+nums[left]==target:
                        if [nums[i],nums[j],nums[left],nums[right]] not in res:
                            res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif nums[i]+nums[j]+nums[right]+nums[left]>target:
                        right-=1
                    else:
                        left+=1
        return res
                        
                