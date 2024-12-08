class Solution:
    
    def swap(self,nums,ind1,ind2):
            temp=nums[ind1]
            nums[ind1]=nums[ind2]
            nums[ind2]=temp
        
    def reversed(self,nums,beg,end):
        while beg<end:
            self.swap(nums,beg,end)
            beg+=1
            end-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        # find pivot from where the number decreases
        pivot = 0
        for i in range(N-1,0,-1):
            if nums[i-1]<nums[i]:
                pivot = i
                break
        
        # sort the array if pvot=0
        if pivot==0:
            nums.sort()
            return
        
        # find swap number
        swap=len(nums)-1
        while nums[pivot-1]>=nums[swap]:
            swap-=1
            
        # swap the number
        self.swap(nums, pivot-1, swap)

        #reverse the number from pivot point to make it lowest from biggets
        self.reversed(nums, pivot, N-1)
        
        return nums
        