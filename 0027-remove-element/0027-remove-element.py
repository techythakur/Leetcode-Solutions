class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=len(nums)-1
        while(i!=0):
            if not nums:
                break
            elif (nums[i] == val):
                nums.pop(i)
            i=i-1
        if not nums:
            nums=[]
        elif nums[0]==val:
            nums.pop(0)
        return len(nums)