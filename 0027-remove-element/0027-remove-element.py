class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]==val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j]= temp
                j-=1
            else:
                i+=1
        return len(nums)-nums.count(val)