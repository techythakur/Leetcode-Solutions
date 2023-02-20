class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return i