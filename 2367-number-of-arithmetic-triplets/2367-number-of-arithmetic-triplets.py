class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]+diff in nums and nums[i]+2*diff in nums:
                count+=1
        return count
        
        '''temp=set()
        lookup={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j]-nums[i]== diff and nums[k]-nums[j]==diff:
                        temp.add((i,j,k))
        return len(temp)'''