class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x={}
        
        for i in range(len(nums)):
            if nums[i] in x:
                if i-x[nums[i]]<=k:
                    return True
                else:
                    x[nums[i]]=i
            else:
                x[nums[i]]=i
        return False