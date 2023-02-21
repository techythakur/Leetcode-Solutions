from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=Counter(nums)
        cnt=0
        for i,j in count.items():
            if j>=2:
                nums[cnt],nums[cnt+1]=i,i
                cnt+=2
            else:
                nums[cnt]=i
                cnt+=1
        return cnt
                
            